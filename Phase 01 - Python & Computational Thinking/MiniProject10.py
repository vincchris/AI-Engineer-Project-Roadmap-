# Mini Project 10 — Personal Finance Manager

total = []
income = []

while True:
  print("==========================")
  print("   PERSONAL FINANCE")
  print("==========================")

  print("""
    1. Add Income
    2. Add Expense
    3. Show Transactions
    4. Show Balance
    5. Show Income
    6. Show Expense
    7. Search Transactions
    8. Exit
""")

  user_input = str(input("Choice : "))

  if user_input == "1":
    def add_income():
      print("==== Add Income ====")
      input_income = int(input("Income : "))

      income_category = {
        "Income": input_income
      }

      income.append(income_category)
      for item in enumerate(income, 1):
        print(f"Income : {item["Income"]}")

  add_income()