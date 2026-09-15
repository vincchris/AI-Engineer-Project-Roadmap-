# Mini Project 01 — Simple Calculator

print("=== CALCULATOR ===")
print("""
  1. Addiction
  2. Substraction
  3. Multiplication
  4. Division
""")

user_input = input(str("Choose : "))

if user_input == "1":
  while True:
    num1 = int(input("Number 1 : "))
    num2 = int(input("Number 2 : "))

    print("The result : ", num1 + num2)
    text = input("Type 'quit' to exit or 'enter' to continue :")
    if text == "quit":
      break
    else:
      continue

elif user_input == "2":
  while True:
    num1 = int(input("Number 1 : "))
    num2 = int(input("Number 2 : "))

    print("The result : ", num1 - num2)
    text = input("Type 'quit' to exit or 'enter' to continue :")
    if text == "quit":
      break
    else:
      continue

elif user_input == "3":
  while True:
    num1 = int(input("Number 1 : "))
    num2 = int(input("Number 2 : "))

    print("The result : ", num1 * num2)
    text = input("Type 'quit' to exit or 'enter' to continue :")
    if text == "quit":
      break
    else:
      continue

elif user_input == "4":
  while True:
    num1 = int(input("Number 1 : "))
    num2 = int(input("Number 2 : "))

    print("The result : ", int(num1 / num2))
    text = input("Type 'quit' to exit or 'enter' to continue :")
    if text == "quit":
      break
    else:
      continue