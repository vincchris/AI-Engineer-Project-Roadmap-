# Mini Project 11 — Number Analyzer

numbers = []
print("====== Number Analyzer =======")
print("Type 'Exit' or space for stoping and return the result")

while True:
  user_input = input("Input a Number : ").strip()

  if user_input == "" or user_input.lower() == "stop":
    break

  try:
    number = int(user_input)
    numbers.append(number)
  except ValueError:
    print("Input isn't valid")

if len(numbers) > 0:
  total_number = sum(numbers)
  average_number = total_number / len(numbers)
  smallest_number = min(numbers)
  highest_number = max(numbers)

  odd_number = 0
  even_number = 0

  for num in numbers:
    if num % 2 == 0:
      even_number += 1
    else:
      odd_number += 1

  print("=" * 20)
  print("Number Analyzer")
  print("=" * 20)

  print(f"List of Numbers : {numbers}")
  print(f"Total of Numbers : {total_number}")
  print(f"Total Count     : {len(numbers)}")
  print(f"Total Average   : {average_number}")
  print(f"The Smallest Number : {smallest_number}")
  print(f"The Highest Number : {highest_number}")
  print(f"Odd Number : {odd_number}")
  print(f"Even Number : {even_number}")
else:
    print("\nTidak ada angka yang dimasukkan.")
