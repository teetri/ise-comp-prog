class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '(' + str(self.value) + ' ' + str(self.suit) + ')'

    def getScore(self):
        if self.value in ['J', 'Q', 'K']:
            return 10
        elif self.value == 'A':
            return 1
        else:
            return int(self.value)

    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10

    def __lt__(self, rhs):
        v = {
            '3': 1,
            '4': 2,
            '5': 3,
            '6': 4,
            '7': 5,
            '8': 6,
            '9': 7,
            '10': 8,
            'J': 9,
            'Q': 10,
            'K': 11,
            'A': 12,
            '2': 13
        }
        s = {
            'club': 1,
            'diamond': 2,
            'heart': 3,
            'spade': 4
        }
        a = v[self.value] * 4 + s[self.suit]
        b = v[rhs.value] * 4 + s[rhs.suit]
        return a < b


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])
