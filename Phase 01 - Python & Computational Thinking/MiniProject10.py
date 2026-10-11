# Mini Project 10 — Personal Finance Manager

total = []
income = []

def add_income():
    print("==== Add Income ====")
    input_income = int(input("Income : "))
    input_income_type = str(input("Category : "))

    income_category = {
      f"{input_income_type}": input_income
    }

    income.append(income_category)
    print("\nIncome Successfully Added")
    # for item in income:
    #   print(f"Added Income : {item["Income"]}")

def add_expense():
    print("===== Add Expense ====")
    add_expense = str(input("Add Expense : "))
    total_expense = int(input("Total : "))

    expense_category = {
      f"{add_expense}": total_expense
    }
    total.append(expense_category)
    print("\nExpense Successfully Added")

def show_transactions():
    print("== Show Transactions ==")
    total_income = 0
    for item in income:
      for value in item.values():
        total_income += value

    total_expense = 0
    for item in total:
      for value in item.values():
        total_expense += value

    balance = total_income - total_expense

    print(f"Total Income : {total_income}")
    print(f"Total Expense : {total_expense}")
    print(f"Net Balance : {balance}")

def show_balance():
  print("== Show Balance ==")
  total_income = 0
  for item in income:
    for value in item.values():
      total_income += value

  total_expense = 0
  for item in total:
    for value in item.values():
      total_expense += value

  balance = total_income - total_expense

  print(f"Net Balance : {balance}")

def show_income():
  print("== Show Income ==")
  total_income = 0
  for item in income:
    for value in item.values():
      total_income += value

  print(f"Total Income : {total_income}")

def show_expense():
  print("== Show Expense ==")
  total_expense = 0
  for item in total:
    for value in item.values():
      total_expense += value

  print(f"Total Expense : {total_expense}")

def search_transactions():
  print("== Search Transactions ==")
  search_engine = str(input("Search : ")).strip().lower()
  found = False

  for item in income:
    for category, amount in item.items():
      if search_engine in category.lower():
        found = True
        print(f"Category : {category}")
        print(f"Amount : {amount}")
        break

  for item in total:
    for category, amount in item.items():
      if search_engine in category.lower():
        found = True
        print(f"Category : {category}")
        print(f"Amount : {amount}")
        break

  if not found:
    print("There isn't Transactions")


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

  user_input = str(input("Choice : ")).strip()

  if user_input == "1":
    add_income()

  elif user_input == "2":
    add_expense()

  elif user_input == "3":
    show_transactions()

  elif user_input == "4":
    show_balance()

  elif user_input == "5":
    show_income()

  elif user_input == "6":
    show_expense()

  elif user_input == "7":
    search_transactions()

  elif user_input == "8":
    print("GoodBye!")
    break

  else:
    print("Please Choose the valid options")