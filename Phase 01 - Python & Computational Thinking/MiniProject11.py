# Mini Project 11 — Number Analyzer

numbers = []
print("====== Number Analyzer =======")
print("Type 'Exit' or space for stoping and return the result")

while True:
  user_input = input("Input a Number : ").strip()

  if user_input == "" and user_input.lower() == "stop":
    break

  try:
    number = int(user_input)
    numbers.append(number)
  except ValueError:
    print("Input isn't valid")

if len(numbers) > 0:
  total_number = sum(numbers)
  average_number = total_number / len(numbers)
  print("=" * 20)
  print("Number Analyzer")
  print("=" * 20)

  print(f"List of Numbers : {numbers}")
  print(f"Total of Numbers : {total_number}")