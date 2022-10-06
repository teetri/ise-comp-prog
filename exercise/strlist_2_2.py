from math import floor

s = str(input())

t = s[0] + s[-1]

u = s[floor(len(s) / 2) - 1]

print(t)
print(u)
