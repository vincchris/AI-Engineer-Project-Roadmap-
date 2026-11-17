# Mini Project 12 — Number Guessing
import random

lowest_num = 1
highest_num = 100
answer = 0
guesses = 0
is_running = True

print("== Number Guessing ==")
print(f"Please select number between {lowest_num} and {highest_num}")

while is_running:

  guess = input("Enter a Number : ")

  if guess.isdigit():
    guess = int(guess)
    guesses += 1

    if guess < lowest_num or guess > highest_num:
      print("The number is out of range")

    elif guess < answer:
      print("Wrong! Try Again")
    elif guess > answer:
      print("Wrong! Try Again")
    else:
      print(f"Correct! The answer was {answer}")
      print(f"Number of guesses {guesses}")
      is_running = False
  else:
    print("Invalid number")
    print(f"Select number between {lowest_num} and {highest_num}")