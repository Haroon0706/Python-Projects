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

score = 0 

# Drawing our initial card out of the deck

card1 = deck.pop(0)

# Using a while loop we can build the bulk of the game in terms of drawing a new card over and over until the player loses

while True:
    os.system("cls")
    print("Your score so far is", score)
    print("\nThe current card is", card1[0])

    # This inner while loop is used to avoid the program not knowing what to do if there is an invalid input
    while True:
        choice = input("\nHigher or lower?")
        if len(choice) > 0:
            if choice[0].lower() in ["h", "l"]:
                break

    card2 = deck.pop(0)
    print("The next card is", card2[0])
    time.sleep(1)

    if choice[0].lower() == "h" and card2[1] > card1[1]:
        print("Correct!")
        score += 1
        time.sleep(1)

    if choice[0].lower() == "h" and card2[1] < card1[1]:
        print("Wrong!")
        time.sleep(1)
        break

    if choice[0].lower() == "l" and card2[1] < card1[1]:
        print("Correct!")
        score += 1
        time.sleep(1)

    if choice[0].lower() == "l" and card2[1] > card1[1]:
        print("Wrong!")
        time.sleep(1)
        break
    if card2[1] == card1[1]:
        print("Draw")

# card2 will become the new card1 in the above loop and as the game continues the next card will take its place

    card1 = card2

# Final overview of game results    

os.system("cls")
print("Game over!")
print("Your final score is", score)
time.sleep(4)
os.system("cls")