class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'


class Rect():
    def __init__(self, p1, p2):
        self.lowerleft = p1
        self.upperright = p2

    def __str__(self):
        return str(self.lowerleft)+'-'+str(self.upperright)

    def area(self):
        return abs((self.upperright.x-self.lowerleft.x)*(self.upperright.y-self.lowerleft.y))

    def __lt__(self, rhs):
        return self.area() < rhs.area()


n = int(input())
rects = []
for i in range(n):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    lowerleft = Point(x1, y1)
    upperright = Point(x2, y2)
    rects.append(Rect(lowerleft, upperright))
rects.sort()
for i in range(n):
    print(rects[i])
