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
from cnf import stuff
conf_file = None
if len(sys.argv) > 1:
    conf_file = stuff[sys.argv[1]] if sys.argv[1] in stuff else None
    utils.prettyprint(conf_file)

af_conf = utils.checkconf(conf_file, "af_config", None)

num_of_runs = utils.checkconf(conf_file, "num_of_runs", 3)
n = utils.checkconf(conf_file, "n", 5) if utils.checkconf(conf_file, "daug", True) else 1
execute_active = utils.checkconf(conf_file, "execute_active", True)
execute_normal = utils.checkconf(conf_file, "execute_random", True)

seeds = utils.checkconf(conf_file, "seeds", [])
if len(seeds) < num_of_runs:
    seeds = seeds + [ numpy.random.randint(0, 2**32-1 ) for x in range(len(seeds), num_of_runs)]

full_classes = utils.checkconf(conf_file, "full_classes", None)
starting_indexes = None
starting_indexes_location = utils.checkconf(conf_file , "starting_indexes_location", "")
if starting_indexes_location != "":
    with open(starting_indexes_location + ".csv", "r") as file:
        r = csv.reader(file)
        starting_indexes = [int(x) for l in r for x in l]

validation_indexes = None
validation_indexes_location = utils.checkconf(conf_file , "validation_indexes_location", "")
if validation_indexes_location != "":
    with open(validation_indexes_location + ".csv", "r+") as file:
        r = csv.reader(file)
        validation_indexes = [int(x) for l in r for x in l]





af_config = {
    "using_ensemble_entropy": utils.checkconf(af_conf, "using_ensemble_entropy", False) if af_conf is not None else False,
    "varratio_weight": utils.checkconf(af_conf, "varratio_weight", 0) if af_conf is not None else 0,
    "distance_weight": utils.checkconf(af_conf, "distance_weight", 1) if af_conf is not None else 1,
    "using_max": utils.checkconf(af_conf, "using_max", False) if af_conf is not None else False,
}

trans_conf = utils.checkconf(conf_file, "trans_config", None)
trans_list = []
if utils.checkconf(trans_conf, "rotation", True):
    trans_list.append(trans.RandomRotation(utils.checkconf(trans_conf, "rotation_degree", 5)))
if utils.checkconf(trans_conf, "crop", True):
    trans_list.append(trans.RandomCrop(utils.checkconf(trans_conf, "crop_amount", 26)))
if utils.checkconf(trans_conf, "gauss", True):
    trans_list.append(utils.Gauss(utils.checkconf(trans_conf, "gauss_mean", 0), utils.checkconf(trans_conf, "gauss_var", 0.1)))
if utils.checkconf(trans_conf, "flip", True):
    trans_list.append(trans.RandomHorizontalFlip())
trans_list.append(trans.Resize((32, 32)))
trans_list.append(trans.ToTensor())

trans_selection_conf = utils.checkconf(conf_file, "selection_trans_config", None)
exclusive_transformations = utils.checkconf(trans_selection_conf, "exclusive_transformations", False)
trans_selection_list = []
if utils.checkconf(trans_selection_conf, "rotation", True):
    trans_selection_list.append(trans.RandomRotation(utils.checkconf(trans_selection_conf, "rotation_degree", 5)))
if utils.checkconf(trans_selection_conf, "crop", True):
    trans_selection_list.append(trans.RandomCrop(utils.checkconf(trans_selection_conf, "crop_amount", 26)))
if utils.checkconf(trans_selection_conf, "gauss", True):
    trans_selection_list.append(utils.Gauss(utils.checkconf(trans_selection_conf, "gauss_mean", 0), utils.checkconf(trans_selection_conf, "gauss_var", 0.1)))
if utils.checkconf(trans_selection_conf, "flip", True):
    trans_selection_list.append(trans.RandomHorizontalFlip())

if not utils.checkconf(trans_selection_conf, "exclusive_transformations", False):
    trans_selection_list.append(trans.Resize((32, 32)))
    trans_selection_list.append(trans.ToTensor())

traintrans_daug = trans.Compose(trans_list)
traintrans_nodaug = trans.Compose([
    trans.ToTensor()
])

selectiontrans_nodaug = trans.Compose([
    trans.ToTensor()
])
selectiontrans_daug = trans.Compose(trans_selection_list)
if utils.checkconf(trans_selection_conf, "exclusive_transformations", False):
    selectiontrans_daug = [trans.Compose([trans_selection_list[x % len(trans_selection_list)], trans.Resize((32, 32)), trans.ToTensor()]) for x in range(n)]
    if utils.checkconf(trans_selection_conf, "original", False):
        selectiontrans_daug.append(selectiontrans_nodaug)
        n = n+1

test_transform = trans.Compose([
    trans.ToTensor()
])

using_prior = utils.checkconf(conf_file, "using_prior", True)
prior_baseline = utils.checkconf(conf_file, "prior_baseline", False)

learning_rate = 0.005
max_number_of_epochs_before_changing_lr = 5
lr_factor = utils.checkconf(conf_file, "lr_factor", 5)

epochs_first_step = utils.checkconf(conf_file, "epochs", 100)
epochs_second_step = utils.checkconf(conf_file, "epochs", 100)

train_batch_size = 32

difficult_classes_percentage = 1 if utils.checkconf(conf_file, "balanced", "bbb")[1] == "b" else utils.checkconf(conf_file, "difficult_classes_percentage", .1)
total_train_data = int(25000 * (1 + difficult_classes_percentage))
train_val_ratio = .9
train_set_percentage = utils.checkconf(conf_file, "train_set_percentage_at_each_iter", 5)

first_time_multiplier = 1
until_slice_number = 8


traintrans_01 = traintrans_daug
selectiontrans = selectiontrans_daug if utils.checkconf(conf_file, "daug", True) else selectiontrans_nodaug

print(selectiontrans)

print("Number of different images at selection phase: " + str(n))


train_set_length = int(train_val_ratio * total_train_data) # int(total_train_data-2000)  # total length of training set data
if utils.checkconf(conf_file, "balanced", "bbb")[1] == "u" and utils.checkconf(conf_file, "balanced", "bbb")[2] == "b":
    train_set_length = int(total_train_data - (utils.checkconf(conf_file, "el_for_validation", 200)*10))
el_for_validation = utils.checkconf(conf_file, "el_for_validation", 200)
balanced_test_set = (utils.checkconf(conf_file, "balanced", "bbb")[2] == "b")


tslp = int((train_set_length * train_set_percentage) / 100)

class CifarLoader():
    def __init__(self, transform=None, first_time_multiplier=1, name=None, unbal=True, test_transform=None, selection_transform=None):
        self._train_val_set = customcifar.UnbalancedCIFAR10(root="./cifar", train=True, download=True, transform=transform, filename=name, percentage=difficult_classes_percentage, valels=el_for_validation, selection_transformations=selection_transform, full_classes=full_classes, startingindexes=starting_indexes, valindexes=validation_indexes)
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



def a_single_experiment(esname, esnumber, seed):
    print("Starting new experiment....")
    print("Setting seed as {0}".format(seed))

    numpy.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

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
    dataset = CifarLoader(transform=traintrans_01,test_transform=test_transform, selection_transform=selectiontrans , first_time_multiplier=first_time_multiplier, name="res/results_{0}_{1}".format(esname, esnumber), unbal=True)

    dataset._train_val_set.use_selection_transforms()
    dataset._train_val_set.use_train_transformation()

    el_for_active = [x for x in dataset.already_selected_indices]
    el_for_normal = [x for x in dataset.already_selected_indices]
    write_dataset_info(dataset, el_for_active, el_for_normal, "res/results_{0}_{1}".format(esname, esnumber))
    best_net, best_acc = single_train_batch(num_of_epochs=epochs_first_step, dataset=dataset,
                                            name="res/results_{0}_{1}".format(esname, esnumber))

    active_net = best_net.clone()
    normal_net = best_net.clone()
    for i in range(first_time_multiplier, until_slice_number):
        active_indices, density_estimator, normal_indices = None, None, None

        if execute_active:
            if not exclusive_transformations:
                dataset._train_val_set.use_selection_transforms()
            active_indices, density_estimator = active_net.distance_and_varratio(dataset,
                                                         [x for x in dataset.train_indices if x not in el_for_active], tslp,
                                                         el_for_active, n=n, config=af_config, execute_active=execute_active, exclusive_transformations=exclusive_transformations)
            dataset._train_val_set.use_train_transformation()

        if execute_normal:
            normal_indices = numpy.random.choice([x for x in dataset.train_indices if x not in el_for_normal], size=tslp, replace=False)
        if active_indices is not None and normal_indices is not None:
            if len(active_indices) < tslp :
                active_indices.extend([x for x in normal_indices if x not in active_indices and x not in el_for_active and len(active_indices) < tslp])
            print("\t\trandom: {0} | loe: {1}".format(len(active_indices), len(normal_indices)))

        if execute_normal:
            el_for_normal.extend(normal_indices)
        if execute_active:
            el_for_active.extend(active_indices)

        write_dataset_info(dataset, el_for_active, el_for_normal, "res/results_{0}_{1}".format(esname, esnumber))
        de_for_normal = normal_net.evaluate_density(dataset, [x for x in dataset.train_indices if x not in el_for_normal], el_for_normal)

        if prior_baseline:
            if utils.checkconf(conf_file, "balanced", "bbb")[2] == "b":
                density_estimator = [1] * 10
            else:
                density_estimator = [1 if x in dataset._train_val_set.full_classes else difficult_classes_percentage for x in range(10)]
            de_for_normal = density_estimator
        print(density_estimator)

        best_nor_acc = 0
        if execute_normal:
            print("NORMAL:")
            best_nor_net, best_nor_acc = single_train_batch(num_of_epochs=epochs_second_step,
                                                        dataset=dataset, indices=el_for_normal,
                                                        name="res/results_{0}_{1}_nor".format(esname, esnumber), test_distro=de_for_normal)
            normal_net = best_nor_net

        best_act_acc = 0
        if execute_active:
            print("ACTIVE:")
            best_act_net, best_act_acc = single_train_batch(num_of_epochs=epochs_second_step, dataset=dataset, indices=el_for_active, name="res/results_{0}_{1}_act".format(esname, esnumber), test_distro=density_estimator)
            active_net = best_act_net

        if execute_active and execute_normal:
            print("Iter: {0} | Active: {1:.2f}  -  Normal: {2:.2f}".format(i, best_act_acc, best_nor_acc))

        # active_net = best_act_net
        # normal_net = best_nor_net

        with open("res/results_{0}_{1}.csv".format(esname, esnumber), "a") as csvfile:
            writer = csv.writer(csvfile)
            if execute_active and execute_normal:
                writer.writerow([i+1, best_act_acc, best_nor_acc, best_act_acc-best_nor_acc])
            elif execute_active:
                writer.writerow([i + 1, best_act_acc, "---", "---"])
            elif execute_normal:
                writer.writerow([i + 1, "---", best_nor_acc, "---"])


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
        isbest, acc = network.validate(i, dataset.validate(), prior=elementsperclass if using_prior else None, targetprior=targetprior if using_prior else None)
        # print("Accuracy so far: {0:.2f}".format(acc))
        if isbest:
            best_network = network.clone()
            num_of_no_improvement = 0
        else:
            num_of_no_improvement += 1
            if num_of_no_improvement == max_number_of_epochs_before_changing_lr:
                mnumber_of_lr_dim += 1
                num_of_no_improvement = 0
                actual_lr /= lr_factor

                for param_group in network.optimizer.param_groups :
                    # network = best_network.clone()
                    print("LR Before: " + str(param_group['lr']))
                    param_group['lr'] = actual_lr
                    print("LR After: " + str(param_group['lr']))

    print("\n\t  TEST:")
    best_acc = network.test(0, dataset.test(), name, prior=elementsperclass if using_prior else None, targetprior=targetprior if using_prior else None)
    print("Test accuracy: {0:.2f}".format(best_acc))

    return best_network, best_acc


# MAIN.....................................................

if len(sys.argv) > 1:
    print("Starting " + str(sys.argv[1]))
    esname = "3_" + str(sys.argv[1]) + "_" + str(datetime.datetime.now().strftime("%B.%d.%Y-%H.%M"))

for i in range(num_of_runs):
    a_single_experiment(esname + "_" + str(epochs_first_step), i, seed=seeds[i])

print("Writing res...")
results = [[] for i in range(num_of_runs)]
for i in range(num_of_runs):
    with open("res/results_{0}_{1}.csv".format(esname + "_" + str(epochs_first_step), i), "r+") as csvfile:
        reader = csv.reader(csvfile)
        results[i] = [row[1] for row in reader]

with open("res/results_{0}_totals.csv".format(esname + "_" + str(epochs_first_step)), "w+") as csvfile:
    writer = csv.writer(csvfile)
    for i in range(len(results[0])):
        writer.writerow([results[j][i] for j in range(num_of_runs)])