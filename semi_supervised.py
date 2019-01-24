import copy

import torch
import torch.utils.data as tud
import torch.nn.functional as F
import torch.nn as nn

import utils
import csv
import numpy
import time

import customcifar
import acquisition_functions


class SemiSupervisedLoss:
    def __init__(self, alpha=1):
        self.alpha = alpha
        self.strong_label_loss = nn.CrossEntropyLoss(reduce=False)
        self.weak_label_loss = nn.CrossEntropyLoss(reduce=False)

    def __call__(self, values, labels, semi_labels, tf, confidence=None ):
        t = self.strong_label_loss(values, labels) * tf
        t2 = self.weak_label_loss(values, semi_labels) * (1-tf) * torch.Tensor(confidence).to("cuda:0")
        return torch.mean(t + (self.alpha * t2))

class ConfidenceVector:
    def __init__(self, N, ground_truth):
        self.cv = [float(1) if i in ground_truth else float(0) for i in range(N)]

    def modify(self, indexes, confidences):
        for i in range(len(indexes)):
            self.cv[indexes[i]] = confidences[i].item()




def generate_cv(N, ground_truth, weak_labels):
    t = [float(1) if i in ground_truth else float(0) for i in range(N)]
    for i in range(len(weak_labels[0])):
        t[weak_labels[0][i]] = weak_labels[1][i].item()
    return t

def generate_semi_target(N, weak_labels):
    t = [0 for i in range(N)]
    for i in range(len(weak_labels[0])):
        t[weak_labels[0][i]] = weak_labels[1][i].item()
    return t


def generate_weak_labels(net, cds, indices, train_indices, n=5):
    net.eval()

    normalized_confidence = [torch.Tensor().to("cuda:0"), torch.Tensor().long().to("cuda:0"), torch.Tensor().long()]
    randomized_list = numpy.random.choice([x for x in indices], len(indices), replace=False)
    dataloaders = [tud.DataLoader(cds.dataset, batch_size=500, shuffle=False, num_workers=4,
                                  sampler=customcifar.CustomSampler(randomized_list)) for i in range(n)]

    c_max = torch.Tensor().to("cuda:0")
    with torch.no_grad():
        for batch_index, element in enumerate(zip(*dataloaders)):  # unlabelled samples
            normalized_confidence[2] = torch.cat((normalized_confidence[2], element[0][2]), 0)

            els = [x for x in element]
            predictions = torch.Tensor().long()

            for input in els:
                input[0], input[1] = input[0].to("cuda:0"), input[1].to("cuda:0")
                output = net(input[0])
                predictions = torch.cat((predictions, output[0].max(1)[1].reshape(len(output[0]), 1).cpu()), 1)

            c = torch.Tensor(acquisition_functions.confidence(predictions.transpose(0,1).to("cuda:0"), details=True)).to("cuda:0") / n
            c_max = torch.cat((c_max, c ), 0)
        c_max = c_max.max(1)
        normalized_confidence[0] = c_max[0]
        normalized_confidence[1] = c_max[1]

        return torch.cat(normalized_confidence, 1)

