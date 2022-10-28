from itertools import combinations


def find_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5


def find_closest_pair(points):
    p = list(combinations(points, 2))
    d = [find_distance(i[0], i[1]) for i in p]
    x = list(zip(p, d))
    x.sort(key=lambda x: x[1])
    x = [i[0] for i in x if i[1] == x[0][1]]
    x = [[points.index(i[0]), points.index(i[1])] for i in x]
    print(x)


find_closest_pair([(30, 30), (30, 31), (31, 30), (30, 32)])
