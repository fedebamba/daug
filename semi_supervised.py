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

    def __call__(self, values, labels, tf, confidence=None ):
        t = self.strong_label_loss(values, labels) * tf
        t2 = self.weak_label_loss(values, labels) * (1-tf)

        print(t)
        print(t2)

        return torch.sum(t + (self.alpha * t2))

        # t = self.strong_label()



def generate_weak_labels(net, cds, indices, train_indices, n=5):
    net.eval()

    normalized_confidence = [torch.Tensor().to("cuda:0"), torch.Tensor().long()]
    randomized_list = numpy.random.choice([x for x in indices], len(indices), replace=False)
    dataloaders = [tud.DataLoader(cds.dataset, batch_size=500, shuffle=False, num_workers=4,
                                  sampler=customcifar.CustomSampler(randomized_list)) for i in range(n)]

    with torch.no_grad():
        for batch_index, element in enumerate(zip(*dataloaders)):  # unlabelled samples
            normalized_confidence[1] = torch.cat((normalized_confidence[1], element[0][2]), 0)

            els = [x for x in element]
            o = torch.Tensor().to("cuda:0")
            predictions = torch.Tensor().long()

            for input in els:
                input[0], input[1] = input[0].to("cuda:0"), input[1].to("cuda:0")
                output = net(input[0])
#                out = output[1].reshape(len(input[0]), 512, 1)

#                o = torch.cat((o, out), 2)
                predictions = torch.cat((predictions, output[0].max(1)[1].reshape(len(output[0]), 1).cpu()), 1)

            normalized_confidence[0] = torch.cat((normalized_confidence[0].cpu(), torch.Tensor(
                acquisition_functions.confidence(predictions.transpose(0,1), details=True)).cpu() / n), 0).cpu()

            normalized_confidence[0] = normalized_confidence[0].max(1)
            print(normalized_confidence)

