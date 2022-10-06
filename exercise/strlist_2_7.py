x = list('1234567890')

x[1::2] = (len(x) // 2) * [0]

print(x)
