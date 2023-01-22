import os
import random
from deck import Deck

#Setup the game
def init_game():
    deck = Deck() #The deck with all the cards
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0

# Initial dealing for player and dealer
    while len(player_cards) < 2:
 
    # Randomly dealing a card
        player_card = deck.pull_card()
        player_cards.append(player_card)
        deck.cards.remove(player_card)
    
        # Updating the player score
        player_score += player_card.numeric_value
    
        #Check if both players first card are aces, in that case reduce value
        #of first to 1 and reduce player score by ten.
        if len(player_cards) == 2:
            if player_cards[0].numeric_value == 11 and player_cards[1].numeric_value == 11:
                player_cards[0].numeric_value = 1
                player_score -= 10

        print("PLAYER CARDS: ")
        for card in player_cards:
            card.print()

    #clear()

# Clear the terminal
def clear():
    os.system("clear")
