import json

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter name: ").strip().title()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!\n")

# View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.\n")
        return
    
    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

# Search for a contact
def search_contact():
    keyword = input("Enter name or phone number to search: ").strip().lower()
    contacts = load_contacts()
    found_contacts = [c for c in contacts if keyword in c["name"].lower() or keyword in c["phone"]]

    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")
    else:
        print("No matching contacts found.\n")

# Update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ").strip().title()
    contacts = load_contacts()

    for contact in contacts:
        if contact["name"] == name:
            print(f"Updating contact: {contact}")
            contact["phone"] = input("Enter new phone number: ").strip() or contact["phone"]
            contact["email"] = input("Enter new email: ").strip() or contact["email"]
            contact["address"] = input("Enter new address: ").strip() or contact["address"]
            
            save_contacts(contacts)
            print(f"Contact '{name}' updated successfully!\n")
            return

    print("Contact not found.\n")

# Delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip().title()
    contacts = load_contacts()

    new_contacts = [c for c in contacts if c["name"] != name]

    if len(new_contacts) == len(contacts):
        print("Contact not found.\n")
    else:
        save_contacts(new_contacts)
        print(f"Contact '{name}' deleted successfully!\n")

# Menu for the Contact Management System
def menu():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

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
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.\n")

# Run the application
menu()
