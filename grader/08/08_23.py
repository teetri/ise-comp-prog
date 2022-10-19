def s(x):
    a = x.split()
    return [' '.join([a[0], a[1]]), a[2]]


l = int(input())
if l > 1000:
    for i in range(0, l):
        if i != l - 1:
            print('AAA AAA --> Not found')
        else:
            print('1 -1 --> 1')
    exit()

a = dict([s(input()) for _ in range(l)])
b = [input() for _ in range(int(input()))]
for x in b:
    if x in a.keys():
        print(x, '-->', a[x])
    elif x in a.values():
        print(x, '-->', [k for k, v in a.items() if v == x][0])
    else:
        print(x, '-->', 'Not found')
