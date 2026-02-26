contacts = {}

def add_contact():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    name = (first_name, last_name)
    contacts[name] = phone
    print(" Contact added successfully")

def view_contact():
    if not contacts:
        print(" No contacts found")
    else:
        print("\n--- Contact List ---")
        for (first, last), phone in contacts.items():
            print(f"{first} {last} : {phone}")

def search_contact():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    key = (first_name, last_name)

    if key in contacts:
        print(f" {first_name} {last_name}s : {contacts[key]}")
    else:
        print(" Contact not found")

while True:
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Exit book")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        print("Exit the contact book")
       
    
    
