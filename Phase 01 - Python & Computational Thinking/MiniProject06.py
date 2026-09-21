# Mini Project 06 — Contact Book

contact = {
  "Name": "",
  "Phone": "",
  "Email": "",
}

while True:
  print("""
    1. Add Contact
    2. Show Contacts
    3. Search Contact
    4. Delete Contact
    5. Exit
""")

  user_input = str(input("Choice : "))

  if user_input == "1":
    print("== Add Contact ==")
    name_input = str(input("Name : "))
    phone_input