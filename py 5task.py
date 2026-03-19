# Contact Book using Python

contacts = []

# Add Contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print(" Contact added successfully!")

# View Contacts
def view_contacts():
    if not contacts:
        print(" No contacts found.")
        return

    print("\n Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

# Search Contact
def search_contact():
    search = input("Enter name or phone to search: ")

    found = False
    for contact in contacts:
        if search.lower() in contact['name'].lower() or search in contact['phone']:
            print("\n Contact Found:")
            print(contact)
            found = True

    if not found:
        print(" Contact not found.")

# Update Contact
def update_contact():
    name = input("Enter name to update: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Enter new details:")
            contact['phone'] = input("New Phone: ")
            contact['email'] = input("New Email: ")
            contact['address'] = input("New Address: ")
            print(" Contact updated!")
            return

    print(" Contact not found.")

# Delete Contact
def delete_contact():
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print(" Contact deleted!")
            return

    print(" Contact not found.")

# Main Menu
while True:
    print("\n=====  Contact Book Menu =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book...")
        break
    else:
        print(" Invalid choice, try again.")