import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as tud

import torchvision.transforms as trans

import sys
import numpy
import copy
import csv
import datetime

import prova_torch_resnet as netter
import customcifar
import net_functions as nf
import utils



# PARAMETER PART................

esname = "exp_Entropy_" + str(datetime.datetime.now().strftime("%B.%d.%Y-%H.%M"))
just100 = True

learning_rate = 0.005
max_number_of_epochs_before_changing_lr = 5
lr_factor = 3

epochs_first_step = 50  # 50
epochs_second_step = 100

train_batch_size = 32

total_train_data = 50000
train_val_ratio = .9
train_set_percentage = 5

first_time_multiplier = 1
until_slice_number = 8

train_set_length = int(train_val_ratio * total_train_data) # int(total_train_data-2000)  # total length of training set data
tslp = int((train_set_length * train_set_percentage) / 100)


traintrans_01 = trans.Compose([
        trans.RandomRotation(5),
        trans.RandomCrop(26),
        trans.Resize((32, 32)),
        utils.Gauss(0, 0.1),
        trans.ToTensor()
    ])
traintrans_02 = trans.Compose([
    trans.RandomRotation(5),
    trans.RandomCrop(26),
    trans.Resize((32, 32)),
    utils.Gauss(0, 0.1),
    trans.ToTensor()
])
test_transform = trans.Compose([
    trans.ToTensor()
])




class CifarLoader():
    def __init__(self, transform=None, first_time_multiplier=1, name=None, unbal=True, test_transform=None):
        self._train_val_set = customcifar.UnbalancedCIFAR10(root="./cifar", train=True, download=True, transform=transform, filename=name, percentage=1, valels=.1)
        self._test_set = customcifar.UnbalancedCIFAR10(root="./cifar", train=False, download=True, transform=test_transform, full_classes=self._train_val_set.full_classes, unbal_test=False)  # 10000

        self.validation_indices = self._train_val_set._val_indices
        self.train_indices = [x for x in self._train_val_set.indices if x not in self.validation_indices]

        print([len([x for x in self.train_indices if x in self._train_val_set.el_for_class[i] ]) for i in range(10)])

        if unbal:
                self.already_selected_indices = numpy.random.choice(self.train_indices, size=tslp*first_time_multiplier, replace=False).tolist()
        else:
                lenel = [int(tslp/10) + (1 if i < tslp % int(tslp/10) else 0) for i in range(10)]
                self.already_selected_indices = [x for i in range(10) for x in numpy.random.choice([xx for xx in self._train_val_set.el_for_class[i] if xx not in self.validation_indices], size=lenel[i], replace=False).tolist()]

        print("Selected: {}".format([len([x for x in self.already_selected_indices if x in self._train_val_set.el_for_class[i]]) for i in range(10)]))


        self._train = tud.DataLoader(self._train_val_set, batch_size=train_batch_size, shuffle=False, num_workers=2,
                                  sampler=customcifar.CustomRandomSampler(self.already_selected_indices))

        self._v = tud.DataLoader(self._train_val_set, batch_size=100, shuffle=False, num_workers=2,
                                          sampler=customcifar.CustomRandomSampler(self.validation_indices))
        self._t = torch.utils.data.DataLoader(self._test_set, batch_size=100, shuffle=False, num_workers=2, sampler=customcifar.CustomSampler([x for x in range(len((self._test_set)))]))

    def clone(self, t):
        other = CifarLoader()
        other._train_val_set = self._train_val_set.clone(t)
        other._test_set=self._test_set
        other.validation_indices= self.validation_indices
        other.train_indices = self.train_indices
        other.already_selected_indices=self.already_selected_indices
        other._train= self._train
        other._v = self._v
        other._t = self._t
        return other

    def all_train(self, otherDS=None, excluded=[]):
        if otherDS is None:
            return tud.DataLoader(self._train_val_set, batch_size=1, shuffle=False,
                                         num_workers=2, sampler=customcifar.CustomSampler([x for x in self.train_indices if x not in excluded]))
        else:
            return tud.DataLoader(otherDS, batch_size=1, shuffle=False,
                                         num_workers=2, sampler=customcifar.CustomSampler([x for x in self.train_indices if x not in excluded]))

    def train(self):
        return self._train

    def validate(self):
        return tud.DataLoader(self._train_val_set, batch_size=100, shuffle=False, num_workers=2,
                                    sampler=customcifar.CustomRandomSampler(self.validation_indices))
    def test(self):
        if self._test_set.indices is not None:
            return torch.utils.data.DataLoader(self._test_set, batch_size=100, shuffle=False, num_workers=2, sampler=customcifar.CustomRandomSampler(self._test_set.indices))
        else:
            return torch.utils.data.DataLoader(self._test_set, batch_size=100, shuffle=False, num_workers=2)


    def select_for_train(self, indices):
        self.already_selected_indices.extend(indices)
        return tud.DataLoader(self._train_val_set, batch_size=train_batch_size, shuffle=False, num_workers=2,
                                    sampler=customcifar.CustomRandomSampler(indices))


# ////////////////////////////////////////////
def new_network():
    # net = netter.ResNet18()
    net = netter.CustomResNet18()
    net = net.to("cuda:0")

    criterion = nn.CrossEntropyLoss()  # probabilmente la dovremo cambiare
    optimizer = optim.SGD(net.parameters(), lr=learning_rate, momentum=0.9, weight_decay=1e-4)

    return nf.NetTrainer(net=net, criterion=criterion, optimizer=optimizer)


def write_dataset_info(ds, active_indices, normal_indices, filename):
    active_els = [0] * 10
    normal_els = [0] * 10

    dataloader_1 = tud.DataLoader(ds._train_val_set, batch_size=1, shuffle=False,
                                  num_workers=2, sampler=customcifar.CustomSampler([x for x in active_indices]))
    dataloader_2 = tud.DataLoader(ds._train_val_set, batch_size=1, shuffle=False,
                                  num_workers=2, sampler=customcifar.CustomSampler([x for x in normal_indices]))

    with torch.no_grad():
        for b, (input, target, i) in enumerate(dataloader_1):
            active_els[target.item()] += 1
        for b, (input, target, i) in enumerate(dataloader_2):
            normal_els[target.item()] += 1

    with open(filename + "_datainfo.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([active_els[i] for i in range(len(active_els))] + [""] + [normal_els[i] for i in range(len(normal_els))])


def a_single_experiment(esname, esnumber):
    with open("res/results_{0}_{1}.csv".format(esname, esnumber), "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Perc", "Active", "Normal", "Delta"])
    with open("res/results_{0}_{1}_datainfo.csv".format(esname, esnumber), "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Active"] + ([""]*10) + ["Normal"])
    with open("res/results_{0}_{1}_nor_per_class.csv".format(esname, esnumber), "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([])
    with open("res/results_{0}_{1}_act_per_class.csv".format(esname, esnumber), "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([])

    # Network def
    net_trainer = new_network()

    # Dataset def
    dataset = CifarLoader(transform=traintrans_01,test_transform=test_transform, first_time_multiplier=first_time_multiplier, name="res/results_{0}_{1}".format(esname, esnumber), unbal=True)
    # dataset_for_active = dataset.clone(traintrans_02)

    el_for_active = [x for x in dataset.already_selected_indices]
    el_for_normal = [x for x in dataset.already_selected_indices]
    write_dataset_info(dataset, el_for_active, el_for_normal, "res/results_{0}_{1}".format(esname, esnumber))
    best_net, best_acc = single_train_batch(num_of_epochs=epochs_first_step, dataset=dataset,
                                            name="res/results_{0}_{1}".format(esname, esnumber))

    active_net = best_net.clone()
    normal_net = best_net.clone()
    for i in range(first_time_multiplier, until_slice_number):
        active_indices, density_estimator = active_net.distance_and_varratio(dataset,
                                                     [x for x in dataset.train_indices if x not in el_for_active], tslp,
                                                     el_for_active, n=5, config={"using_ensemble_entropy": True})

        normal_indices = numpy.random.choice([x for x in dataset.train_indices if x not in el_for_normal], size=tslp, replace=False)
        if len(active_indices) < tslp :
            active_indices.extend([x for x in normal_indices if x not in active_indices and x not in el_for_active and len(active_indices) < tslp])

        print("\t\trandom: {0} | loe: {1}".format(len(active_indices), len(normal_indices)))
        el_for_active.extend(active_indices)
        el_for_normal.extend(normal_indices)

        write_dataset_info(dataset, el_for_active, el_for_normal, "res/results_{0}_{1}".format(esname, esnumber))

        de_for_normal = normal_net.evaluate_density(dataset, [x for x in dataset.train_indices if x not in el_for_normal], el_for_normal)

        # density_estimator = [1] * 10
        # de_for_normal = density_estimator
        print(density_estimator)


        print("NORMAL:")
        best_nor_net, best_nor_acc = single_train_batch(num_of_epochs=epochs_second_step,
                                                        dataset=dataset, indices=el_for_normal,
                                                        name="res/results_{0}_{1}_nor".format(esname, esnumber), test_distro=de_for_normal)
        print("ACTIVE:")

        best_act_net, best_act_acc = single_train_batch(num_of_epochs=epochs_second_step, dataset=dataset, indices=el_for_active, name="res/results_{0}_{1}_act".format(esname, esnumber), test_distro=density_estimator)
        print("Iter: {0} | Active: {1:.2f}  -  Normal: {2:.2f}".format(i, best_act_acc, best_nor_acc))

        active_net = best_act_net
        normal_net = best_nor_net

        with open("res/results_{0}_{1}.csv".format(esname, esnumber), "a") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([i+1, best_act_acc, best_nor_acc, best_act_acc-best_nor_acc])


def single_train_batch(num_of_epochs=10, dataset=None, indices=None, name=None, test_distro=None):
    network = new_network()
    best_network = network.clone()
    mnumber_of_lr_dim = 0
    num_of_no_improvement = 0
    actual_lr = learning_rate

    elementsperclass = []
    targetprior = torch.Tensor([1] * 10).to("cuda:0") if test_distro is None else torch.Tensor(test_distro).to("cuda:0")   # torch.Tensor([1 if x in dataset._test_set.full_classes else .1 for x in range(10)]).to("cuda:0")
    for i in range(num_of_epochs):
        print("\n\t  TRAIN:  {0} - lr: {1:.5f}, chances: {2}".format(i, actual_lr, max_number_of_epochs_before_changing_lr - num_of_no_improvement) )
        if indices is None:
            elementsperclass = network.train(i, dataset.train())
        else:
            elementsperclass = network.train(i, dataset.select_for_train(indices))
        print("\t  VALIDATION:   " + str(i))
        isbest, acc = network.validate(i, dataset.validate(), prior=elementsperclass, targetprior=targetprior)
        # print("Accuracy so far: {0:.2f}".format(acc))
        if isbest:
            best_network = network.clone()
            num_of_no_improvement = 0
        else:
            num_of_no_improvement += 1
            if num_of_no_improvement == max_number_of_epochs_before_changing_lr:
                mnumber_of_lr_dim += 1
                num_of_no_improvement = -mnumber_of_lr_dim
                actual_lr /= lr_factor

                for param_group in network.optimizer.param_groups :
                    # network = best_network.clone()
                    print("LR Before: " + str(param_group['lr']))
                    param_group['lr'] = actual_lr
                    print("LR After: " + str(param_group['lr']))

    print("\n\t  TEST:")
    best_acc = network.test(0, dataset.test(), name, prior=elementsperclass, targetprior=targetprior)
    print("Test accuracy: {0:.2f}".format(best_acc))

    return best_network, best_acc


# MAIN.....................................................

if len(sys.argv) > 1:
    print("Starting " + str(sys.argv[1]))
    esname = "3_" + str(sys.argv[1]) + "_" + str(datetime.datetime.now().strftime("%B.%d.%Y-%H.%M"))

if not just100:
    for i in range(3):
        a_single_experiment(esname + "_" + str(epochs_first_step), i)

epochs_first_step = 100
epochs_second_step = 100

for i in range(3):
    a_single_experiment(esname + "_" + str(epochs_first_step), i)
