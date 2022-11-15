class Complex():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        rpart = self.a
        ipart = self.b
        sign = '+'
        if self.b < 0:
            sign = ''

        if rpart == 0 and ipart != 0:
            rpart = ''
            sign = ''
        if ipart == 0:
            return str(rpart)
        if ipart == 1:
            ipart = ''
        if ipart == -1:
            ipart = '-'

        return str(rpart) + sign + str(ipart) + 'i'

    def __add__(self, rhs):
        rpart = self.a + rhs.a
        ipart = self.b + rhs.b
        sign = '+'
        if ipart < 0:
            sign = ''

        if rpart == 0:
            rpart = ''
            sign = ''
        if ipart == 0:
            return str(rpart)
        if ipart == 1:
            ipart = ''
        if ipart == -1:
            ipart = '-'

        return str(rpart) + sign + str(ipart) + 'i'

    def __mul__(self, rhs):
        rpart = self.a * rhs.a - self.b * rhs.b
        ipart = self.a * rhs.b + self.b * rhs.a
        sign = '+'
        if ipart < 0:
            sign = ''

        if rpart == 0:
            rpart = ''
            sign = ''
        if ipart == 0:
            return str(rpart)
        if ipart == 1:
            ipart = ''
        if ipart == -1:
            ipart = '-'

        return str(rpart) + sign + str(ipart) + 'i'

    def __truediv__(self, rhs):
        a, b, c, d = self.a, self.b, rhs.a, rhs.b
        rpart = (a*c + b*d)/(c**2 + d**2)
        ipart = (b*c - a*d)/(c**2 + d**2)
        sign = '+'
        if ipart < 0:
            sign = ''

        if rpart == 0:
            rpart = ''
            sign = ''
        if ipart == 0:
            return str(rpart)
        if ipart == 1:
            ipart = ''
        if ipart == -1:
            ipart = '-'

        return str(rpart) + sign + str(ipart) + 'i'

# def main():
#     u = Complex(1, 2)
#     v = Complex(3, 4)

#     print(str(u))
#     print(u + v)
# main()


t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if t == 1:
    print(c1)
elif t == 2:
    print(c2)
elif t == 3:
    print(c1 + c2)
elif t == 4:
    print(c1 * c2)
else:
    print(c1 / c2)
