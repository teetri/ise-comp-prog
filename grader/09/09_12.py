a = [set(input().split()) for _ in range(int(input()))]
if a != []:
    print(len(set.union(*a)), '\n', len(set.intersection(*a)))
else:
    print(0, '\n', 0)
