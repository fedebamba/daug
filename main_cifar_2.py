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




transform=trans.Compose([trans.ToTensor()])
name = None # todo
difficult_classes_percentage = .1
el_for_validation = 20
selection_transformations = trans.Compose([trans.ToTensor()])
full_classes= None # todo
starting_indexes = None # todo
validation_indexes = None # todo
balanced_test_set = False #todo

tslp = 50 # todo
train_batch_size = 32


class CifarLoader():
    def __init__(self, transform=None, first_time_multiplier=1, name=None, unbal=True, test_transform=None, selection_transform=None):
        self._train_val_set = customcifar.UnbalancedCIFAR100(root="./cifar", train=True, download=True, transform=transform, filename=name, percentage=difficult_classes_percentage, valels=el_for_validation, selection_transformations=selection_transform, full_classes=full_classes, startingindexes=starting_indexes, valindexes=validation_indexes)
        self._test_set = customcifar.UnbalancedCIFAR10(root="./cifar", train=False, download=True, transform=test_transform, full_classes=self._train_val_set.full_classes, unbal_test=(not balanced_test_set))  # 10000

        self.validation_indices = self._train_val_set._val_indices
        self.train_indices = [x for x in self._train_val_set.indices if x not in self.validation_indices]

        print([len([x for x in self.train_indices if x in self._train_val_set.el_for_class[i] ]) for i in range(10)])

        if unbal:
             # self.already_selected_indices = numpy.random.choice(self.train_indices, size=tslp*first_time_multiplier, replace=False).tolist()
             if starting_indexes is not None:
                 print(starting_indexes)
                 self.already_selected_indices = [x for x in starting_indexes]
             else:
                self.already_selected_indices = self._train_val_set.define_starting_set(forced_distribution=True)
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



if __name__ == "__main__":
    x = customcifar.UnbalancedCIFAR100(root="./cifar100", transform=trans.Compose([trans.ToTensor()]))
