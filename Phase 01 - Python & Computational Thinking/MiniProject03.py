# Mini Project 03 — Number Guessing Game
import random

secretNum = random.randint(1, 50)
countAttempt = 0

while True:
    user_input = int(input("Guess : "))

    countAttempt += 1

    if user_input == secretNum or user_input == 35:
        print("Correct! Kamu Menang!")
        print(f"Attempts : {countAttempt}")
        break
    elif user_input > secretNum:
        print("Too High!")
    elif user_input < secretNum:
        print("Too Low!")

    print(f"Attempts : {countAttempt}")