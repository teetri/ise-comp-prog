import numpy as np

answer = ""  # @param {type:"raw"}


def f1(x, a):
    x[np.where(x == np.min(x))] = a
    print(x)


f1(np.array([1, 2, 3, 1, 5, 3]), 9)


def f2(x):
    n = len(x)
    d = np.ndarray((n, n), x.dtype)
    for i in range(n):
        for j in range(n):
            d[i, j] = x[i] + x[j]
    return d


# print(f2(np.array([2, 5, 3, 1, 5])))


def f3(x):
    n = len(x)
    d1 = np.array([x] * n)
    d2 = np.transpose(d1)
    # print(d1)
    # print(d2)
    d3 = d1 + d2
    # print(d3)
    return d3


# f3(np.array([2, 5, 3, 1, 5]))

def f4_3(x, a, b):
    print(x)
    y = np.logical_and(a <= x, x <= b)
    print(y)

    m = x[np.logical_and(a <= x, x <= b)]
    print(m)


# f4_3(np.array([10, 20, 30, 40, 50, 60, 70]), 30, 50)

def eq(a, b, p):
    c = a == b
    print(c)
    d = sum(c) / np.size(a) * 100
    print(d)
    print(d >= p)


# a = np.array([1, 2, 3, 4, 5])
# b = np.array([0, 8, 3, 4, 2])
# eq(a, b, 41)


class Path():
    def __init__(self, src, dest, cost):
        if src > dest:
            src, dest = dest, src
        self.src = src
        self.dest = dest
        self.cost = cost

    def __str__(self):
        return '|'+self.src+'| <-- '+str(self.cost)+' --> |'+self.dest+'|'

    def __lt__(self, other):
        return self.cost > other.cost


def testpath():
    print('list of paths...')
    paths = [
        Path('A', 'K', 3), Path('A', 'J', 7), Path(
            'B', 'C', 1), Path('B', 'F', 7),
        Path('C', 'D', 2), Path('C', 'G', 6), Path(
            'D', 'J', 8), Path('E', 'F', 1),
        Path('F', 'H', 4), Path('G', 'I', 3), Path(
            'G', 'K', 5), Path('H', 'I', 2),
        Path('H', 'K', 5)
    ]
    paths.sort()
    for p in paths:
        print(p)
