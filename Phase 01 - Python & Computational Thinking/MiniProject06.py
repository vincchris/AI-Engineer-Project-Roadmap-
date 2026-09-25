contacts = []

while True:
    print("""
    1. Add Contact
    2. Show Contacts
    3. Search Contact
    4. Delete Contact
    5. Exit
""")

    user_input = input("Choice : ").strip()

    # --- 1. ADD CONTACT ---
    if user_input == "1":
        print("== Add Contact ==")
        name_input = input("Name : ").strip()
        phone_input = input("Phone : ").strip()
        email_input = input("Email : ").strip()

        new_contact = {
            "Name": name_input,
            "Phone": phone_input,
            "Email": email_input
        }

        contacts.append(new_contact)
        print("\nContact saved successfully!")

    # --- 2. SHOW CONTACTS ---
    elif user_input == "2":
        print("== Show Contacts ==")
        if not contacts:
            print("No contacts found.")
        else:
            for idx, item in enumerate(contacts, 1):
                print(f"\n[{idx}]")
                print(f"Name  : {item['Name']}")
                print(f"Phone : {item['Phone']}")
                print(f"Email : {item['Email']}")

    # --- 3. SEARCH CONTACT ---
    elif user_input == "3":
        print("== Search Contact ==")
        search_input = input("Search Name : ").strip().lower()
        found = False

        for item in contacts:
            if search_input in item["Name"].lower():
                print(f"\nName  : {item['Name']}")
                print(f"Phone : {item['Phone']}")
                print(f"Email : {item['Email']}")
                found = True

        if not found:
            print("Contact Doesn't Exist")

    # --- 4. DELETE CONTACT ---
    elif user_input == "4":
        print("== Delete Contact ==")
        delete_input = input("Enter Name to Delete : ").strip().lower()
        found = False

        for item in contacts:
            if item["Name"].lower() == delete_input:
                contacts.remove(item)
                print(f"Contact '{item['Name']}' deleted successfully!")
                found = True
                break

        if not found:
            print("Contact Not Found")

    # --- 5. EXIT ---
    elif user_input == "5":
        print("GoodBye!")
        break

    else:
        print("Choose a Valid Option (1 - 5)!")