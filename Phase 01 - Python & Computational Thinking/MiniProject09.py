# Mini Project 09 - Quiz Game

quiz_list = [
  {
    "no": 1,
    "title": "What is the output 2 + 3?",
    "options": {
      "A": 4,
      "B": 5,
      "C": 6,
      "D": 7,
    },
    "answer": "B"
  },
  {
    "no": 2,
    "title": "What is the output 8 - 2?",
    "options": {
        "A": 10,
        "B": 1,
        "C": 6,
        "D": 7,
      },
    "answer": "C"
  }
]

score = 0
correct = 0
wrong = 0

while True:
  for quiz in quiz_list:
    print("Quiz Game")
    print(f"Question No : {quiz["no"]}")

    print(f"{quiz['title']}")

    for key, value in quiz['options'].items():
      print(f"{key}. {value}")

    user_input = str(input("Choice (A/B/C/D) : ")).upper()

    if user_input == quiz['answer']:
      correct += 1
      score += 10
      print(f"+{score} points")
    else:
      wrong += 1
      score -= 10

  if quiz != quiz['options']:
    break

print("== Quiz Result ==")
print(f"Correct = {correct}")
print(f"Wrong = {wrong}")
print(f"Score = {score}")
