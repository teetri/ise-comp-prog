import numpy as np


def mult_table(nrows, ncols):
    return np.array([[i*j for j in range(1, ncols+1)] for i in range(1, nrows+1)])


exec(input().strip())
