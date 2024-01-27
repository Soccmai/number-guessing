from art import logo
import random
import os


def start_game():
    global tries
    global lost
    lost = False
    global number
    number = random.randint(1, 100)
    print(logo)
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. ")
    if difficulty == 'easy':
        tries = 10
    elif difficulty == 'hard':
        tries = 5


game_continues = True

while game_continues:
    os.system('cls')
    start_game()
    while tries > 0:
        print(f"Tries remaining: {tries}")
        guess = int(input("Guess a number: "))
        if guess == number:
            print("Good job! You won!")
            tries = -1
        if guess < number:
            print("Too low!\n")
        elif guess > number:
            print("Too high!\n")
        tries -= 1

    if tries == 0:
        print("Try again!")

    if input("Do you want to continue? Enter 'y' if yes or 'n' if no. ") == 'n':
        game_continues = False
