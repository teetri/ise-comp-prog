import numpy as np


def peak_indexes(x):
    b1 = (x[1:-1] - x[:-2]) > 0
    b2 = (x[1:-1] - x[2:]) > 0
    return np.arange(1, x.shape[0]-1)[b1 & b2]


def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(d)
    if len(pos) > 0:
        print(', '.join([str(e) for e in pos]))
    else:
        print('No peaks')


exec(input().strip())
# print(peak_indexes(np.array([1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1])))
