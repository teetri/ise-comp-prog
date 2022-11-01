a = list(zip(*((input().split()) for _ in range(int(input())))))
print(sorted(list(set(a[0])-set(a[1]))))
