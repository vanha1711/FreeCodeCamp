import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        list = np.array(list).reshape((3, 3))

        mean = [list.mean(axis=0).tolist(), list.mean(axis=1).tolist(), list.mean().tolist()]
        var = [list.var(axis=0).tolist(), list.var(axis=1).tolist(), list.var().tolist()]
        std = [list.std(axis=0).tolist(), list.std(axis=1).tolist(), list.std().tolist()]
        max = [list.max(axis=0).tolist(), list.max(axis=1).tolist(), list.max().tolist()]
        min = [list.min(axis=0).tolist(), list.min(axis=1).tolist(), list.min().tolist()]
        sum = [list.sum(axis=0).tolist(), list.sum(axis=1).tolist(), list.sum().tolist()]

        calculations = {"mean": mean, "variance": var, "standard deviation": std, "max": max, "min":min, "sum":sum}

    return calculations

