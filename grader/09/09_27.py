def read_relations():
    x = {}
    while True:
        a = input().split()
        if a == ['q']:
            break
        if a[0] in x:
            x[a[0]].add(a[1])
        else:
            x[a[0]] = set(a[1])
    all_people = set(x.keys()).union(*x.values())
    for i in all_people:
        if i not in x:
            x[i] = set()
    return x


def knows(R, x, y):
    return y in R[x]


def is_celeb(R, x):
    return all(knows(R, y, x) for y in R if y != x) and (R[x] == set() or R[x] == {x})


def find_celeb(R):
    for x in R:
        if is_celeb(R, x):
            return x
    return None


def main():
    R = read_relations()
    c = find_celeb(R)
    if c is None:
        print('Not Found')
    else:
        print(c)


exec(input().strip())
