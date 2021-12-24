import random

suit = ["Spades", "Clubs", "Diamonds", "Hearts"]
value = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
deck = []
countdown = 52
done = False

def pickCard():
    return random.choice(value) + " of " + random.choice(suit)

while countdown > 0:
    a = pickCard()
    if a in deck:
        pass
    else:
        deck.append(a)
        countdown -=1

print(deck)
print(len(deck))