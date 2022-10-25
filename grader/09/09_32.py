def first_fit(L, e):
    for x in L:
        if sum(x) + e <= 100:
            x.append(e)
            return None
    L.append([e])


def best_fit(L, e):
    if len(L) == 0:
        L.append([e])
        return None

    best = L.index(min(L, key=lambda x: sum(x)))
    a = False
    for i in range(len(L)):
        if sum(L[i]) + e <= 100 and (sum(L[best]) + e) <= (sum(L[i]) + e):
            best = i
            a = True
            # print('#', best, i, L[best], L[i])
    if a:
        L[best].append(e)
    else:
        L.append([e])


def partition_FF(D):
    L = []
    for e in D:
        first_fit(L, e)
    return L


def partition_BF(D):
    L = []
    for e in D:
        best_fit(L, e)
    return L


# L = [[51], [60]]
# best_fit(L, 49)
# print(L)

exec(input().strip())
