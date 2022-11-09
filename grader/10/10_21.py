import numpy as np
import calendar


def sum_2_rows(A):
    B = np.zeros((A.shape[0] // 2, A.shape[1]), dtype=int)
    for i in range(0, A.shape[0], 2):
        B[i // 2, :] = A[i, :] + A[i + 1, :]
    return B


def sum_left_right(A):
    return A[:, A.shape[1] // 2:] + A[:, :A.shape[1] // 2]


def sum_upper_lower(A):
    return A[A.shape[0] // 2:, :] + A[:A.shape[0] // 2, :]


def sum_4_quadrants(A):
    return A[:A.shape[0] // 2, :A.shape[1] // 2] + A[:A.shape[0] // 2, A.shape[1] // 2:] + A[A.shape[0] // 2:, :A.shape[1] // 2] + A[A.shape[0] // 2:, A.shape[1] // 2:]


def sum_4_cells(A):
    B = np.zeros((A.shape[0] // 2, A.shape[1] // 2), dtype=int)
    for i in range(0, B.shape[0], 1):
        for j in range(0, B.shape[1], 1):
            B[i, j] = np.sum(A[i*2:i*2+2, j*2:j*2+2])
    return B


def count_leap_years(A):
    return np.sum(np.array([calendar.isleap(y - 543) for y in A]))


exec(input().strip())
