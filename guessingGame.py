# importing tandom
import random

# intializing the number of chances
chances = 5

#printing number guessing game
print("Number guessing game")
print("Number of chances: ",chances)
print("Guess a numberbetween 1 an 9")
number = (random.randint(1,9))

while chances != 0:
    guess = input("Enter your guess:- ")
    # when the guess is same as the number
    if guess == number:
        # if number entered by user is same as the generated number
        # number by randint function then break from loop using loop
        # control statement "break"
        print("Congratulation You Won")
        break
    if guess != number:
        print("Your guess was wrong")
        chances-=1
        print("Chances left :- ",chances)
        continue

if chances == 0:
    print("You Loose!!! The number was:- ",number)