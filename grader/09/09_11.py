a = [input() for _ in range(int(input()))]
b = []
for x in a:
    n = 0
    for y in x:
        if y == '.':
            n += 1
        else:
            break
    b.append(x[n//2:])
print('\n'.join(b))
