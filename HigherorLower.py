# Creating a higher or lower card game

# Time module - use of time weights, OS module - CLS (clear screen in between picking cards) & Random module - need for random picking of cards

import time, os, random

# Creating the deck of cards using a nested for loop
# By using a 2D list we are able to give a value to each of the cards with Ace being a low card valued at 1

ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
deck = []

value = 1
for rank in ranks:
    for suit in suits:
        deck.append([rank + " of " + suit, value])
    value = value + 1

# Using the random module we can shuffle the deck

random.shuffle(deck)
