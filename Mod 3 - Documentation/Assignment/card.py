import random

class Card:
    """
        Represents a single playing card.
        Initialised by passing a suit and a number.
    """

    def __init__(self, suit, number):
        self._suit = suit
        self._number = number

    def __repr__(self):
        return self._number + " of " + self._suit

    @property
    def suit(self):
        """ Returns a string representation of suit. """
        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        """ Returns a string representation of number. """
        return self._number

    @number.setter
    def number(self, number):
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")




class Deck:
    """
        Represents a collection of Cards stacked in order.
    """

    def __init__(self):
        self._cards = []
        self.populate()

    def populate(self):
        """ Populates the suit, numbers, deck of cards with a list. """
        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def shuffle(self):
        """ Randomly shuffles the cards. """
        random.shuffle(self._cards)

    def deal(self, no_of_cards):
        """ Deals and returns the cards. """
        dealt_cards = []
        for i in range(no_of_cards):
            dealt_card = self._cards.pop(0)
            dealt_cards.append(dealt_card)
        return dealt_cards

    def __repr__(self):
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"
        
deck = Deck()
print(deck)

