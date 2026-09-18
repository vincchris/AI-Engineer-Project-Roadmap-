# Mini Project 04 — Simple ATM

print("=== ATM ===")
print("""
  1. Check Balance
  2. Deposit
  3. Withdraw
  4. Exit
""")

while True:

  user_input = str(input("Choose : "))
  balance = 1000000

  if user_input == "1":
    print(f"Balance : {balance}")

  elif user_input == "2":
    deposit = int(input("Deposit : "))
    print(f"Deposit : {balance + deposit}")

  elif user_input == "3":
    withdraw = int(input("Withdraw : "))
    print(f"Withdraw : {balance - withdraw}")

  else:
    print("GoodBye!")
    break