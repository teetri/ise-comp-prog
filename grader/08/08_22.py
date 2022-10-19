a = dict([input().split() for _ in range(int(input()))])
b = [input().split() for _ in range(int(input()))]
c = {}
for (x, y) in b:
    if x in a.keys():
        if x not in c.keys():
            c[x] = int(y) * int(a[x])
        else:
            c[x] += int(y) * int(a[x])

if c == {}:
    print('No ice cream sales')
    exit()

print('Total ice cream sales: ', float(sum(c.values())))

m = max(c.values())
ms = sorted([x[0] for x in c.items() if x[1] == m])
print('Top sales:', ', '.join(ms))
