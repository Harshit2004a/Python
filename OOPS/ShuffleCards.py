# Shuffle a deck of card with OOPS in Python

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.cards = [Card(s, r) for s in self.suits for r in self.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def show(self):
        for card in self.cards:
            print(card)

if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    deck.show()

# Code by Harshit