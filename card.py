# card
from dataclasses import dataclass
from enum import Enum

#Card values
class CardValue(Enum):
    ONE = "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    KNIGHT = "Knight"
    QUEEN = "Queen"
    KING = "King"
    ACE = "Ace"

#Card suit (colors)
class CardSuit(Enum):
    HEARTS = "♡"
    DIAMONDS = "♢"
    SPADES = "♠"
    CLUBS = "♣"

print(__name__)

#The card dataclass
@dataclass
class Card:
    suit: CardSuit
    value: CardValue
    numeric_value: int
    #initiate a card
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.numeric_value = self.get_value(value)
    
    #Print card suit and value
    def print(self):
        return f"{self.suit.value} {self.value.value}"

    @staticmethod
    def get_value(value: CardValue):
        if value.ONE:
            return 1
        if value.TWO:
            return 2
            return 3
        if value.FOUR:
            return 4
        if value.FIVE:
            return 5
        if value.SIX:
            return 6
        if value.SEVEN:
            return 7
        if value.EIGHT:
            return 8
        if value.NINE:
            return 9
        if value.TEN:
            return 10
        if value.KNIGHT:
            return 10
        if value.QUEEN:
            return 10
        if value.KING:
            return 10
        if value.ACE:
            return 11