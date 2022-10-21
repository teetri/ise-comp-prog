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
    for (a, b) in sorted(pocket.items(), key=lambda x: x[0], reverse=True):
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
    # p.sort()
    p = sorted(p.items(), key=lambda x: x[0], reverse=True)
    for x in p:
        pocket[x[0]] -= x[1]

    return {x[0]: x[1] for x in p}


exec(input().strip())
