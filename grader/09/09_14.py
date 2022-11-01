def _d(a): return dict(x.strip().split(',') for x in a)


with open(input(), 'r') as f1, open(input(), 'r') as f2, open(input(), 'r') as f3:
    c, t, db = _d(f1.readlines()), _d(f2.readlines()), [
        x.strip().split(',') for x in f3.readlines()]
print('\n'.join([','.join([c[x[0]], t[x[1]]]) if x[0]
                 in c and x[1] in t else 'record error' for x in db]))
