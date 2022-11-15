class Piggybank():
    def __init__(self):
        self.coins = {
        }

    def add(self, v, n):
        v = float(v)
        if n + sum(self.coins.values()) > 100:
            return False
        if v not in self.coins:
            self.coins[v] = 0
        self.coins[v] += n
        return True

    def __str__(self):
        return '{' + ', '.join([str(v) + ':' + str(self.coins[v]) for v in sorted(self.coins.keys())]) + '}'

    def __float__(self):
        return float(sum([v * self.coins[v] for v in self.coins]))


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = Piggybank()
p2 = Piggybank()
for c in cmd1:
    eval(c)
for c in cmd2:
    eval(c)
