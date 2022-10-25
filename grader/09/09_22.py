def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m


def mult_c(c, A):
    m = []
    for r in A:
        m.append([c*e for e in r])
    return m


def mult(A, B):
    m = []
    for r in A:
        m.append([])
        for j in range(len(B[0])):
            s = 0
            for k in range(len(B)):
                s += r[k]*B[k][j]
            m[-1].append(s)
    return m


exec(input().strip())
