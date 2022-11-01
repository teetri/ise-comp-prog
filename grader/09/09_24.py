x = []
while True:
    a = input().split(', ')
    if a == ['q']:
        break
    if a[1] in [i[0] for i in x]:
        x[[i[0] for i in x].index(a[1])][1].append(a[0])
    else:
        x.append([a[1], [a[0]]])
for i in x:
    print(i[0], ': ', ', '.join(i[1]), sep='')
