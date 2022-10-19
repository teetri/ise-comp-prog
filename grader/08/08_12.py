l = int(input())
if l > 1000:
    print("Not found\n" * l)
    exit()
a = dict([input().split() for _ in range(l)])
b = [input() for _ in range(int(input()))]
for x in b:
    if x in a.keys():
        print(a[x])
    elif x in a.values():
        print([k for k, v in a.items() if v == x][0])
    else:
        print('Not found')
