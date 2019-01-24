import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as tud

import torchvision.transforms as trans

import numpy
import copy
import csv
import datetime
import sys

import prova_torch_resnet as netter
import customcifar
import net_functions as nf
import semi_supervised
import utils

num_of_classes = 10
val_percentage = .2

initial_percentage = .3
iteration_step = .1

learning_rate = 0.001
num_of_epochs = 2

filename = "semi_supervised_75.csv"

transform = trans.Compose([
        trans.RandomRotation(5),
        trans.RandomCrop(26),
        trans.Resize((32, 32)),
        utils.Gauss(0, 0.05),
        trans.ToTensor()
    ])



class CompleteDataset:
    def __init__(self):
        self.dataset = customcifar.CustomCIFAR10(root="./cifar", train=True, download=True, transform=transform)
        self.testset = customcifar.CustomCIFAR10(root="./cifar", train=False, download=True, transform=transform) # palindromo!

        dataloader = tud.DataLoader(self.dataset, batch_size=64, shuffle=False, num_workers=2,
                                    sampler=customcifar.CustomRandomSampler([x for x in range(len(self.dataset))]))
        el_for_class = [[] for x in range(num_of_classes)]
        for batch_index, (inputs, targets, index) in enumerate(dataloader):
            for t in range(len(targets)):
                el_for_class[targets[t]].append(index[t].item())

        val_els_per_class = int((len(self.dataset) * val_percentage) / num_of_classes)

        self.validation_indices = [el for xl in el_for_class for el in numpy.random.choice(xl, size=val_els_per_class, replace=False)]
        self.remaining_indices = [x for x in range(len(self.dataset)) if x not in self.validation_indices]
        self.train_indices = numpy.random.choice(self.remaining_indices, size=int(len(self.remaining_indices)*initial_percentage  ), replace=False)

        print("Dataset loaded: train length {0}/{3} | validation length {1} | test length {2}".format(len(self.train_indices), len(self.validation_indices), len(self.testset), len(self.remaining_indices)))

    def add_to_train(self, indices):
        indices = [x for x in indices if x in self.remaining_indices and x not in self.train_indices]
        self.train_indices.resize(len(self.train_indices) + len(indices))
        self.train_indices[-len(indices):] = indices

    def get_train_loader(self):
        return tud.DataLoader(self.dataset, batch_size=64, shuffle=False, num_workers=2, sampler=customcifar.CustomRandomSampler(self.train_indices))

    def get_validation_loader(self):
        return tud.DataLoader(self.dataset, batch_size=64, shuffle=False, num_workers=2,
                              sampler=customcifar.CustomRandomSampler(self.validation_indices))

    def get_test_loader(self):
        return tud.DataLoader(self.testset, batch_size=64, shuffle=False, num_workers=2,
                              sampler=customcifar.CustomRandomSampler([x for x in range(len(self.testset))]))


def new_net_semisupervised():
    net = netter.CustomResNet18()
    net = net.to("cuda:0")

    criterion_train = semi_supervised.SemiSupervisedLoss(alpha=.5)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=learning_rate, momentum=0.9, weight_decay=1e-4)

    return nf.NetTrainerSemiSupervised(net=net, criterion=criterion, optimizer=optimizer, criterion_train= criterion_train)


def single_train_pass(cd):
    trainloader = cd.get_train_loader()
    validationloader = cd.get_validation_loader()

    net = new_net_semisupervised()
    best_net = net.clone()
    for i in range(num_of_epochs):
        print("Epoch: " + str(i))
        # net.train_semisupervised(i, trainloader)
        net.train(i, trainloader)

        isbest, acc = net.validate(i, validationloader)
        print("\tAccuracy so far: {0:.2f}".format(acc))

        if isbest:
            best_net = net.clone()

    return best_net


def single_train_pass_semi(cd, ol, cv, st):
    trainloader = cd.get_train_loader()
    validationloader = cd.get_validation_loader()

    guess_acc = 0

    net = new_net_semisupervised()
    best_net = net.clone()
    for i in range(num_of_epochs):
        print("Epoch: " + str(i))
        guess_acc = net.train_semisupervised(i, trainloader, ol, cv, st)

        isbest, acc = net.validate(i, validationloader)
        print("Accuracy so far: {0:.2f}".format(acc))

        if isbest:
            best_net = net.clone()

    return best_net, guess_acc



# ====================================================================== #
# ---------------------------------------------------------------------- #
# ====================================================================== #


if len(sys.argv) > 1:
    print("Starting " + str(sys.argv[1]))
    filename = str(sys.argv[1]) + "_" + str(datetime.datetime.now().strftime("%B.%d.%Y-%H.%M")) + ".csv"


cd = CompleteDataset()

ind = [x for x in cd.remaining_indices if x not in cd.train_indices][:int(len(cd.remaining_indices)*.1)]


print(len(cd.train_indices))

# ground truth
original_labels = copy.deepcopy(cd.train_indices)

net = single_train_pass(cd) # Supervised training
net_control = net.clone()

print("\n\t  TEST:")
best_acc = net.test(0, cd.get_test_loader())
print("Test accuracy: {0:.2f}".format(best_acc))

with open("res/" + filename, "w+") as file:
    writer = csv.writer(file)
    writer.writerow(["Iter","Els","Control", "Semi", "Guess"])

for iteration_index in numpy.arange(initial_percentage, .9, iteration_step):
    # get new elements for the training set
    #       ind = [x for x in cd.remaining_indices if x not in cd.train_indices][:int(len(cd.remaining_indices)*iteration_step)] # active learning methods here?
    new_labels_generator = semi_supervised.generate_weak_labels(net=net.net, cds=cd, indices=[x for x in cd.remaining_indices if x not in cd.train_indices], train_indices=[], n=10)
    print(new_labels_generator.size())

    cd.add_to_train(ind)


    # get the weak labels with semi_supervised.generate_weak_labels
    #      new_labels_generator = semi_supervised.generate_weak_labels(net=net.net, cds=cd, indices=ind, train_indices=[], n=10)
    confidence = semi_supervised.generate_cv(len(cd.dataset), original_labels, [new_labels_generator[2], new_labels_generator[0]])
    semi_target = semi_supervised.generate_semi_target(len(cd.dataset), [new_labels_generator[2], new_labels_generator[1]])

    # train and test the control network
    print("\nTrain Control Network")
    net_control = single_train_pass(cd)
    print("\tTest: ")
    best_acc_control = net_control.test(0, cd.get_test_loader())

    # train the semi supervised learning network
    print("\nTrain Semi-supervised Network")
    net, guess_acc = single_train_pass_semi(cd, original_labels, confidence, semi_target)
    print("\tTest: ")
    best_acc = net.test(0, cd.get_test_loader())

    with open("res/" + filename, "a+") as file:
        writer = csv.writer(file)
        writer.writerow([initial_percentage*100, len(cd.train_indices), best_acc_control, best_acc, guess_acc])
