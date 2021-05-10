# Creating a simple dice rolling generator using the random module 

# Instead of importing the entire module we will import the randint method specifically

from random import randint

# Initial question for the simulator

quest = input("Do you want to roll the dice? (Y/N) ")

# Rolling the dice based off the user's input

while quest[0].upper() == "Y":
    print(f"You rolled a {randint(1, 6)}")
    quest = input("Would you like to roll again? (Y/N)")

else:
    if quest[0].upper() == "N":
        print("Thank you for rolling with us!")
