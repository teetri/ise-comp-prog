def total(pocket):
    return sum([int(x[0]) * x[1] for x in pocket.items()])


def take(pocket, money_in):
    for x in money_in.items():
        if x[0] in pocket.keys():
            pocket[x[0]] += x[1]
        else:
            pocket[x[0]] = x[1]


def pay(pocket, amt):
    if total(pocket) < amt:
        return {}

    p = {}
    for (a, b) in pocket.items():
        while amt >= a:
            if b > 0:
                b -= 1
                amt -= a
                if a in p.keys():
                    p[a] += 1
                else:
                    p[a] = 1
            else:
                break
    for x in p.items():
        pocket[x[0]] -= x[1]

    return p


# exec(input().strip())

exec(
    "def _a(p):\n print([(k,v) for k,v in sorted(p.items())])\np={100:3, 10:5, 5:10, 1:7};_a(pay(p, 52));_a(p)")
