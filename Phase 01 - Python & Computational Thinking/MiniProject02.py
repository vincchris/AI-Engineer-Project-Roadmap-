# Mini Project 02 — Student Grade Calculator

subject = ["Math", "English", "Programming", "Language"]
grades = []

print(f"Mata Pelajaran yang tersedia : {', '.join(subject)}")
print("Type 'quit' if u want to stop")

while True:
  user_input = input(str("Input a Subject : "))

  if user_input.lower() == "quit":
    break

  if user_input in subject:
    number_input = int(input("Input a Number : "))
    grades.append(number_input)
    print(f"Nilai Input User : {number_input}")
  else:
    print(f"Subject TIdak Ditemukan")


if grades:
  average = sum(grades) / len(grades)
  highest = max(grades)
  lowest = min(grades)

  if average >= 90:
    print("Grade : A")
  elif average >= 80:
    print("Grade : B")
  elif average >= 60:
    print("Grade : C")
  else:
    print("Grade : D")

  print(f"Average : {average}")
  print(f"Highest : {highest}")
  print(f"Lowest : {lowest}")