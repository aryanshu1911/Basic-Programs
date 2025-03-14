# Program to create a Contact Book...

# create an empty dictionary to store contact details
contacts = {}

# Infinite loop to keep the app running until exit
while True:
    print("\tContact Book Menu")
    print("==================================")
    print("1. Create Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # to create new contact
    if choice == 1:
        name = input("Enter name: ")
        if name in contacts:
            print(f"Contact '{name}' already exists!")
        else:
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contacts[name] = {'Phone Number': int(phone_number), 'Email': email, 'Address': address}
            print(f"Contact '{name}' created successfully!")    
        print()

    # to view the list of all contact names with phone numbers
    elif choice == 2:
        print()
        if not contacts:
            print("No contacts available.")
        else:        
            for name, phone in contacts.items():
                print(f"{name} : {phone['Phone Number']}")
        print()

    # to search for a contact's details in the contact book
    elif choice == 3:
        search_name = input("Enter contact name to search: ")
        found = False
        for name, phone in contacts.items():
            if search_name in name:
                print(f"Found - Name {name}, Phone Number: {phone_number}, Email: {email}, Address:{address}")
                found = True
        if not found:
            print("Contact not found!")
        print()
        
    # to edit details of a contact
    elif choice == 4:
        search_contact = input("Enter name to edit: ")
        if search_contact in contacts:
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contacts[name] = {'Phone Number': int(phone_number), 'Email': email, 'Address': address}
        else:
            print("Contact not found!")
        print()

    # to delete an existing contact
    elif choice == 5:
        name = input("Enter contact name to be deleted: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} has been deleted successfully!")
        else:
            print("Contact not found!")
        print()

    # to exit the program
    elif choice == 6:
        print("Closing the program...")
        break
    
    else:
        print("Inavlid input!")

print()
print("Contact Book Closed.\nGoodbye!")
