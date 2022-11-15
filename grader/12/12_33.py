class Piggybank():
    def __init__(self):
        self.wallet = {
            '1': 0,
            '2': 0,
            '5': 0,
            '10': 0,
        }

    def add1(self, n):
        self.wallet['1'] += n

    def add2(self, n):
        self.wallet['2'] += n

    def add5(self, n):
        self.wallet['5'] += n

    def add10(self, n):
        self.wallet['10'] += n

    def __str__(self):
        return '{1:' + str(self.wallet['1']) + ', 2:' + str(self.wallet['2']) + ', 5:' + str(self.wallet['5']) + ', 10:' + str(self.wallet['10']) + '}'

    def __int__(self):
        return self.wallet['1'] + self.wallet['2']*2 + self.wallet['5']*5 + self.wallet['10']*10

    def __lt__(self, rhs):
        return int(self) < int(rhs)


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = Piggybank()
p2 = Piggybank()
for c in cmd1:
    eval(c)
for c in cmd2:
    eval(c)
