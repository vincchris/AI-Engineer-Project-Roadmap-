# Mini Project 05 — To-Do List CLI

agenda = []

while True:
  print("=== TODO LIST ===")
  print("""
    1. Add Task
    2. Show Task
    3. Complete Task
    4. Delete Task
    5. Exit
  """)

  user_input = str(input("Choice : "))


  if user_input == "1":
    print("== Add Task ==")
    input_task = str(input(" "))
    agenda.append(input_task)
    print(agenda)

  elif user_input == "2":
    print("== Show Task ==")
    if not agenda:
      print("There isn't To Do List")
    else:
      for i, task in enumerate(agenda, start=1):
        print(f"{i}. {task}")

  elif user_input == "3":
    print("== Complete Task ==")
    if not agenda:
      print("There isn't To Do List")
    else:
      for i, task in enumerate(agenda, start=1):
        print(f"{i}. {task}")

      num = int(input("Choose Task are Done : ")) - 1

      if num <= 0 < len(agenda):
        completed = agenda.pop(num)
        print(f"Task is Completed : {completed}")
      else:
        print("Number isn't valid")

  elif user_input == "4":
    print("== Delete Task ==")
    if not agenda:
      print("There isn't List")
    else:
      agenda.clear()
      print("All Task Deleted")

  elif user_input == "5":
    print("Goodbye!")
    break

  else:
    print("Choose isn't valid! Please Choose 1 - 5")