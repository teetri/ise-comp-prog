import numpy as np


def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data


def report_lower_than_mean(weight, data):
    data[:, 1] = np.average(data[:, 1:], axis=1, weights=weight)
    data = data[:, :2]
    data[:, 1] = data[:, 1] < np.average(data[:, 1])
    if np.sum(data[:, 1]) == 0:
        print('None')
        return
    print(', '.join([str(x[0]) for x in data if x[1]]))


exec(input().strip())
