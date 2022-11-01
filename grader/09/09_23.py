def _a(x):
    x = x.strip().split(', ')
    x = [x[-2], [int(i) for i in x[-1].split(':')]]
    x = [x[0], x[1][0]*60+x[1][1]]
    return x


def _b(x):
    if len(str(x)) == 1:
        return '0'+str(x)
    return str(x)


a = [_a(input()) for _ in range(int(input()))]

b = {}
for x in a:
    if x[0] in b:
        b[x[0]] += x[1]
    else:
        b[x[0]] = x[1]

for x in sorted(b, key=b.get, reverse=True)[:3]:
    print(x, ' --> ', b[x]//60, ':', _b(b[x] % 60), sep='')
