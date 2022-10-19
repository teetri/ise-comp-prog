def text2keys(text):
    text = text.lower()
    l = [[' '], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], [
        'm', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    m = []
    for x in text:
        for y in l:
            if x in y:
                z1 = l.index(y)
                z2 = y.index(x) + 1
                m.append([z1, z2])

    m = [str(x[0]) * x[1] for x in m]
    m = ' '.join(m)
    return m


def keys2text(keys):
    l = [[' '], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], [
        'm', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
    m = keys.split()
    m = [l[int(x[0])][len(x) - 1] for x in m]
    m = ''.join(m)
    return m


exec(input().strip())
