def row_number(t, e):
    for i in range(len(t)):
        if e in t[i]:
            return i
    return -1


def flatten(t):
    return [e for r in t for e in r if e != 0]


def inversions(x):
    n = 0
    for i in range(len(x) - 1):
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                n += 1
    return n


def solvable(t):
    a = len(t) % 2 != 0 and inversions(flatten(t)) % 2 == 0
    b = len(t) % 2 == 0 and (inversions(
        flatten(t)) + row_number(t, 0)) % 2 != 0
    return a or b


exec(input().strip())
