# Mini Project 13 — Text Analyzer

text = []
print("======== Text Analyzer ==========")
print("Type 'Exit' or space for stoping and return the result")

while True:
  user_input = input(str("Input a Text : ")).strip()

  if user_input == "" or user_input.lower == "stop":
    break

  