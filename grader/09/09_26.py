from collections import OrderedDict


def _a(x):
    x = x.split(': ')
    x = [x[0], [i for i in x[1].split(', ')]]
    return x


a = OrderedDict([_a(input()) for _ in range(int(input()))])
b = input()
c = []
for j in a:
    for i in a[b]:
        if i in a[j]:
            c.append(j)

d = []
for x in c:
    if x not in d and x != b:
        d.append(x)
if d == []:
    print('Not Found')
else:
    print(*d, sep='\n')
