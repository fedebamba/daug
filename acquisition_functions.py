import torch.nn.functional as F
import torch as T

import numpy


def entropy(net_out):
    sm = F.softmax(net_out)
    logsm = T.log(sm)
    return -T.sum(sm * logsm, 1)

def avg_entropy(net_out):
    e = numpy.zeros(shape=len(net_out[0]))
    for el in net_out:
        sm = F.softmax(el)
        logsm = numpy.log2(sm)
        f = T.mul(T.tensor(sm).to("cuda:0"), T.tensor(logsm).to("cuda:0")).double()
        e = e - T.sum(f.cpu(), 1)
    return e/len(net_out)

def marginals(vector, num_of_classes=10, n=5):
    # la media per i marginali
    ps = T.nn.Softmax(1)(vector)
    ps = T.mean(ps, 2).reshape(len(ps), 10)

    # il primo ed il secondo elemento più grande
    maximums = T.topk(ps, k=2, dim=1)[0]
    marginals = maximums[:, 0] - maximums[:, 1]

    marginals = 1 - marginals
    return marginals

def confidence(vector, num_of_classes=10, details=False):
    if not details:
        return [max([(len([i[v] for i in vector if i[v] == j])) for j in range(num_of_classes)]) for v in range(len(vector[0]))]
    else:
        res = [[(len([i[v] for i in vector if i[v] == j])) for j in range(num_of_classes)] for v in range(len(vector[0]))]
        return res, [max(el) for el in res]



def avg_KL_divergence():
    pass




def max_variance(net_out):
    # it's the same as bestofn
    pred = [out.max(1)[1] for out in net_out]
    return 1 - (confidence(pred)/len(net_out))




def entropic_distance(net_out):
    sm = F.softmax(net_out[0])
    logsm = numpy.log2(sm)
    e = - T.mul(T.tensor(sm).to("cuda:0"), T.tensor(logsm).to("cuda:0")).double().cpu()

    sm = F.softmax(net_out[1])
    logsm = numpy.log2(sm)
    f = - T.mul(T.tensor(sm).to("cuda:0"), T.tensor(logsm).to("cuda:0")).double().cpu()

    ee = T.sum((e - f).abs(), 1)
    return ee
