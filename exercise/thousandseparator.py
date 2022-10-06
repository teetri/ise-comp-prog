s = input()
for i in range(len(s), 0, -3):
    if i - 3 > 0:
        s = s[:i - 3] + ',' + s[i - 3:]

print(s)
