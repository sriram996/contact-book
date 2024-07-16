contacts = {}

def display_menu():
    print("-*-Contact_Book-*")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    
    print(f"Contact {name} added successfully.")

def view_contacts():
    if contacts:
        print("\nContacts:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print("-------------------")
    else:
        print("No contacts found.");

def update_contact():
    name = input("Enter the name of the contact to update: ")
    
    if name in contacts:
        new_phone = input(f"Enter new phone number for {name}: ")
        contacts[name] = new_phone
        print(f"Contact {name} updated successfully.")
    else:
        print(f"No contact found with the name {name}.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"No contact found with the name {name}.")

def search_contact():
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        print(f"Contact found - Name: {name}, Phone: {contacts[name]}")
    else:
        print(f"No contact found with the name {name}.")

def contact_book():
    while True:
        display_menu()
        choice = int(input("Enter choice (1/2/3/4/5/6): "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            update_contact()
        elif choice == 4:
            delete_contact()
        elif choice == 5:
            search_contact()
        elif choice == 6:
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Run the contact book
contact_book()
