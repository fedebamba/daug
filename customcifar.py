
import torchvision
import torch.utils.data as tud

import math
import numpy
import csv
import utils
from cnf import stuff
import sys


class CustomCIFAR10(torchvision.datasets.CIFAR10):

    def __init__(self, root, train=True, transform=None, target_transform=None, download=False, indices=None, percentage=0.0, other=False):
        super().__init__(root=root,
                         train=train,
                         transform=transform,
                         target_transform=target_transform,
                         download=download)


    def __getitem__(self, index):
        (img, target) = super().__getitem__(index)
        return img, target, index

    def __len__(self):
        return super().__len__()

    def __repr__(self):
        return super().__repr__()



class UnbalancedCIFAR10(torchvision.datasets.CIFAR10):
    def __init__(self, root, train=True, transform=None, target_transform=None, download=False, provided_indices=None, num_full_classes=5, percentage=.1, valels=200, filename=None, full_classes=None, unbal_test=False, selection_transformations=None, valindexes=None, startingindexes=None):
        super().__init__(root=root,
                         train=train,
                         transform=transform,
                         target_transform=target_transform,
                         download=download)
        self.train_trans = transform
        self.sel_trans = selection_transformations
        self.indices=None
        self.have_to_cycle=False
        self.transformation_index=0

        if train:
            if provided_indices is not None:
                self._val_indices = provided_indices[1]
                self.indices = provided_indices[0]
                self.el_for_class = None

            else:
                if full_classes is None:
                    full_classes = numpy.random.choice([x for x in range(10)], size=num_full_classes,replace=False)
                self.full_classes = full_classes
                print("Full classes: {0}".format(self.full_classes))

                el_for_class = [[] for x in range(10)]
                data_loader = tud.DataLoader(self, batch_size=100, shuffle=False, num_workers=2,
                                             sampler=CustomSampler([x for x in range(len(self.train_data))]))

                for batch_index, (input, target, i) in enumerate(data_loader):
                    for x in range(len(input)):
                        el_for_class[target[x].item()].append(i[x].item())

                for i in range(len(el_for_class)):
                    if i not in full_classes:
                        if valindexes is not None:
                            el_for_class_tmp = [x for x in el_for_class[i] if (x in valindexes or x in startingindexes)]
                            print("Already selected for {0}: {1} ".format(i , str(len(el_for_class_tmp))))
                            el_for_class_tmp.extend(el_for_class[i][:int( (len(el_for_class[i])*percentage) - len(el_for_class_tmp))])
                            print("Now  : " + str(len(el_for_class_tmp)))
                            el_for_class[i] = el_for_class_tmp
                        else:
                            el_for_class[i] = el_for_class[i][:int((len(el_for_class[i])*percentage))]


                print(["{0}:{1}".format(i, len(el_for_class[i])) for i in range(10)])

                if valindexes is not None:
                    self._val_indices = valindexes
                else:
                    if type(valels) is int:
                        self._val_indices = [x for el in el_for_class for x in numpy.random.choice(el, valels, False)]
                    elif type(valels) is float:
                        self._val_indices = [x for el in el_for_class for x in numpy.random.choice(el, int(len(el) * valels), False)]
                    with open("val_indexes_bbb.csv", "w+") as file:
                        writer = csv.writer(file)
                        for i in range(10):
                            writer.writerow([x for x in el_for_class[i] if x in self._val_indices])


                self.indices = [x for el in el_for_class for x in el]
                self.el_for_class = el_for_class

                # self.train_data = self.train_data[self.indices]
                if filename is not None:
                    with open(filename + "_per_class.csv", "w") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(["100 %" if x in full_classes else "{0} %".format(int(percentage * 100)) for x in range(10)])

            print('Train data ' + str(len(self.train_data)))
            print("Train els: {0}".format([len(el) for el in self.el_for_class]) )
        elif unbal_test:
            print("Creating unbalanced test set......")
            self.full_classes = full_classes

            el_for_class = [[] for x in range(10)]
            data_loader = tud.DataLoader(self, batch_size=100, shuffle=False, num_workers=2,
                                         sampler=CustomSampler([x for x in range(len(self.test_data))]))

            for batch_index, (input, target, i) in enumerate(data_loader):
                for x in range(len(input)):
                    el_for_class[target[x].item()].append(i[x].item())

            for i in range(len(el_for_class)):
                if i not in full_classes:
                    el_for_class[i] = el_for_class[i][:int(len(el_for_class[i]) * percentage)]
            print(["{0}:{1}".format(i, len(el_for_class[i])) for i in range(10)])
            self.indices = [x for el in el_for_class for x in el]

    def use_selection_transforms(self, number=0):
        print("Using selection-time image transformations....")
        if isinstance(self.sel_trans, type([])):
            self.transform = self.sel_trans[number]
        else:
            self.transform = self.sel_trans
        print(self.transform)

    def use_train_transformation(self):
        print("Using training-time image transformations....")
        self.transform = self.train_trans
        print(self.transform)

    def define_starting_set(self, el_percentage=.05, forced_distribution=False):
        if forced_distribution:
            train_els = [[el for el in self.el_for_class[i] if el not in self._val_indices] for i in range(10)]

            with open("starting_indexes_bbb.csv", "w+") as file:
                writer = csv.writer(file)
                for el in train_els:
                    writer.writerow(el[:int(len(el) * el_percentage)])
            return [item for el in train_els for item in el[:int(len(el) * el_percentage)]]


    def clone(self, t):
        other = UnbalancedCIFAR10(root=self.root, train=self.train, transform=t, target_transform=self.target_transform, download=False)
        other._val_indices= self._val_indices
        other.indices=self.indices
        other.el_for_class=self.el_for_class
        return other

    def __getitem__(self, index):
        if self.have_to_cycle:
            self.use_selection_transforms(self.transformation_index)
            self.transformation_index = (self.transformation_index + 1) % len(self.sel_trans)
        (img, target) = super().__getitem__(index)
        return img, target, index

    def __len__(self):
        return super().__len__()

    def __repr__(self):
        return super().__repr__()



class CustomSampler(tud.Sampler):
    def __init__(self, data_source):
        self.data_source = data_source

    def __iter__(self):
        return iter(self.data_source)

    def __len__(self):
        return len(self.data_source)


class CustomRandomSampler(tud.Sampler):
    def __init__(self, data_source):
        arr = numpy.random.choice(data_source, len(data_source), False)
        self.data_source = arr

    def __iter__(self):
        return iter(self.data_source)

    def __len__(self):
        return len(self.data_source)

    def refresh(self):
        self.data_source = numpy.random.choice(self.data_source, len(self.data_source), False)