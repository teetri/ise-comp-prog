import numpy as np
persons = ['A', 'B', 'C', 'D', 'E']


def generate_adjacency_matrix(filename):
    with open(filename, 'r') as f:
        lines = np.array(f.readlines())
    # print(lines)

    def _a(line):
        line = line.strip().split(',')
        return line
    rel = np.array([_a(line) for line in lines])
    # print(rel)

    keys = sorted(list(set(rel.flatten())))
    # print(keys)

    d = {k: i for i, k in enumerate(keys)}
    # print(d)

    m = np.zeros((len(keys), len(keys)), dtype=int)
    # print(m)

    rel2 = np.array([[d[r[0]], d[r[1]]] for r in rel])
    # print(rel2)

    r, c = zip(*rel2)
    m[r, c] = 1
    m[c, r] = 1
    # print(m)

    # m2 = np.sum(m, axis=0)
    # print(m2)

    # m3 = np.diag(m2)
    # print(m3)

    A = m
    person_names = keys

    return A, person_names


def get_degree_matrix(A):
    A = np.sum(A, axis=0)
    A = np.diag(A)
    D = A
    return D


def get_names_with_highest_number_of_friends(D, person_names):
    D = np.sum(D, axis=0)
    p = np.where(D == np.max(D))
    # print(p)
    all_max = [tuple([person_names[i], i]) for i in p[0]]

    return all_max


def get_distance_matrix(Lp):
    m = np.array(Lp)
    keys = np.array(persons)
    # print(m)
    # print(keys)

    # d = {k: i for i, k in enumerate(keys)}
    # print(d)

    o = (len(keys), len(keys))

    # nl = np.sum(m, axis=1)
    # print(nl)

    # rel = np.array(np.meshgrid(keys, keys)).T.reshape(-1, 2)
    # rel2 = np.array([[d[r[0]], d[r[1]]] for r in rel])
    # print(rel2)

    # r, c = zip(*rel2)
    # print(r)
    # print(c)

    # print(np.sum(m[0] & m[1]))
    # print(np.sum(m[0] | m[1]))
    def _b(r, c):
        # print(r, c)
        return np.sum(m[r] & m[c]) / np.sum(m[r] | m[c])
    output = [_b(r, c) for r, c in np.ndindex(o)]
    output = np.array(output).reshape(o)
    np.fill_diagonal(output, 0)
    distance_matrix = output
    # # output[r, c] = r + c
    # output[r, c] = np.sum(m[r] & m[c]) / np.sum(np.sum(m[r] | m[c]))

    return distance_matrix


def get_all_most_similar_pairs(Dt, persons):
    Dt = np.triu(Dt)
    # Dt[0, 0] = 0.6
    # print(Dt)
    p = np.where(Dt == np.max(Dt))
    if len(p[0]) == 1:
        p = [[p[0][0], p[1][0]]]
    # p = np.array([sorted(x) for x in p])
    p = np.array([(persons[x[0]], persons[x[1]]) for x in p])
    pairs = [tuple(sorted(x)) for x in p]
    # print(p)
    return pairs


def main():
    a = generate_adjacency_matrix('social_network.txt')
    print(a)
    b = get_degree_matrix(a[0])
    print(b)
    c = get_names_with_highest_number_of_friends(b, a[1])
    print(c)
    Lp = [[[0, 1, 0, 1, 1, 1, 0],
          [1, 0, 0, 1, 0, 1, 1],
          [0, 0, 0, 0, 1, 0, 1],
          [1, 1, 0, 0, 1, 0, 0],
          [0, 1, 1, 1, 0, 1, 0]], ['A', 'B', 'C', 'D', 'E']]
    Lp = Lp[0]
    d = get_distance_matrix(Lp)
    print(d)
    e = get_all_most_similar_pairs(d, Lp[1])
    print(e)


main()
