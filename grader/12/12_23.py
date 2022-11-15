class Card():

    v = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
    d = [(x, y) for x in v for y in ['club', 'diamond', 'heart', 'spade']]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.score = self.d.index((value, suit))

    def __str__(self):
        return '(' + str(self.value) + ' ' + str(self.suit) + ')'

    def next1(self):
        return Card(*Card.d[(self.score + 1) % 52])

    def next2(self):
        self.score = (self.score + 1) % 52
        self.value = self.d[self.score][0]
        self.suit = self.d[self.score][1]


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
