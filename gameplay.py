import os
from deck import Deck

#Setup the game
def init_game():
    deck = Deck() #The deck with all the cards
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0

    clear()

# Clear the terminal
def clear():
    os.system("clear")
