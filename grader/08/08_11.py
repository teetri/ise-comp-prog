def reverse(d):
    return dict((b, a) for a, b in d.items())


def keys(d, v):
    return [a for a, b in d.items() if b == v]


exec(input().strip())
