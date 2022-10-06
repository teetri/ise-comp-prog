x = list('1234567')

print(x, id(x))

x[2:5] = []

print(x, id(x))
