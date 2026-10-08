# Mini Project 07 — Expense Tracker

total = []

while True:
  print("""
    1. Add Expense
    2. Show Expenses
    3. Total Expense
    4. Search Expense
    5. Exit
""")

  user_input = input("Choice : ")

  if user_input == "1":
    print("== Add Expense ==")
    add_expenses = str(input("Category : "))
    total_expenses = int(input("Total : "))

    category = {
      f"{add_expenses}": total_expenses
    }

    total.append(category)
    print("\nExpense Saved Successfully")

  elif user_input == "2":
    print("== Show Expense ==")
    if not total:
      print("No Expenses Found!")
    else:
      for idx, item in enumerate(total, 1):
        print(f"\n[{idx}]")
        for category_name, nominal in item.items():
          print(f"{category_name} : {nominal}")

  elif user_input == "3":
    print("== Total Expense ==")
    if not total:
      print("No Expenses Found!")
    else:
      total_amount = 0
      for item in total:
        for nominal in item.values():
          total_amount += nominal
      print(f"Total Expense : {total_amount}")

  elif user_input == "4":
    print("== Search Expenses ==")
    search_expenses = str(input("Search Expense : "))
    found = False

    for item in total:
      if search_expenses in item:
        print(f"{search_expenses} : {item[search_expenses]}")
        found = True
        break

    if not found:
      print("There isn't Expenses Data")

  elif user_input == "5":
    print("GoodBye!")
    break

  else:
    print("Please input valid option")
