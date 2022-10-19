import re
s = input().lower().replace(' ', '')
s = re.sub(r'[^a-zA-Z]', '', s)
n = []
for x in s:
    if x not in [x[0] for x in n]:
        n.append([x, s.count(x)])
n.sort(key=lambda x: x[0])
n.sort(key=lambda x: x[1], reverse=True)

for x in n:
    print(x[0], '->', x[1])
