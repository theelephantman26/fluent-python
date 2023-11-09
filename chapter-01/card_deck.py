import collections

Card = collections.namedtuple("Card", ["suit", "rank"])

class FrenchDeck:
    ranks = [str(i) for i in range(2, 11)] + list("JQKA")
    suits = "spades diamonds hearts clubs".split(" ")

    def __init__(self):
        self._cards = [Card(suit=suit, rank=rank) for suit in self.suits for rank in self.ranks]
        pass

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    


# Create a deck
deck = FrenchDeck()

# How big is the deck?
print(f"The Length of the this french deck is {len(deck)}")

# Randomly draw a card from the deck
from random import choice 

print(f"A random draw from the deck is {choice(deck)}")
print(f"A random draw from the deck is {choice(deck)}")

# Print every card in the deck
for i in range(10):
    print(deck[i])
