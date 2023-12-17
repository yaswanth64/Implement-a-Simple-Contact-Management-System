import json

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        contact = {
            'name': name,
            'phone_number': phone_number,
            'email': email
        }
        self.contacts.append(contact)
        print(f"Contact added: {name}")

    def view_contacts(self):
        print("Contact List:")
        for idx, contact in enumerate(self.contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}")

    def edit_contact(self, index, name, phone_number, email):
        if 1 <= index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact['name'] = name
            contact['phone_number'] = phone_number
            contact['email'] = email
            print(f"Contact updated: {name}")
        else:
            print("Invalid index.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            deleted_contact = self.contacts.pop(index - 1)
            print(f"Contact deleted: {deleted_contact['name']}")
        else:
            print("Invalid index.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            pass

# Example usage:
contact_manager = ContactManager()
contact_manager.load_from_file('contacts.json')  # Load existing contacts

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Save and Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email address: ")
        contact_manager.add_contact(name, phone_number, email)
    elif choice == '2':
        contact_manager.view_contacts()
    elif choice == '3':
        index = int(input("Enter the index of the contact to edit: "))
        name = input("Enter new name: ")
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contact_manager.edit_contact(index, name, phone_number, email)
    elif choice == '4':
        index = int(input("Enter the index of the contact to delete: "))
        contact_manager.delete_contact(index)
    elif choice == '5':
        contact_manager.save_to_file('contacts.json')  # Save contacts to file before quitting
        print("Contacts saved. Exiting.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
