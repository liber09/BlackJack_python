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
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)
    
        # Updating the player score
        player_score += player_card.card_value
    
        # In case both the cards are Ace, make the first ace value as 1 
        if len(player_cards) == 2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value = 1
                player_score -= 10

    clear()

# Clear the terminal
def clear():
    os.system("clear")
