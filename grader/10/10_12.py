import numpy as np


def toCelsius(f):
    return (f - 32) * 5 / 9


def BMI(wh):
    return wh[:, 0] / (wh[:, 1] / 100) ** 2


def distanceTo(p, Points):
    return np.sqrt(np.sum((p - Points) ** 2, axis=1))


exec(input().strip())
