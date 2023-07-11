class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print("")

    def search_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                found_contacts.append(contact)
        if not found_contacts:
            print("Contact not found.")
        else:
            print("Matching contacts:")
            for contact in found_contacts:
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print("")

    def delete_contact(self, name):
        deleted_contacts = []
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                deleted_contacts.append(contact)
        if not deleted_contacts:
            print("Contact not found.")
        else:
            print("Deleted contacts:")
            for contact in deleted_contacts:
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print("")

def main():
    contact_manager = ContactManager()

    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            contact = Contact(name, phone, email)
            contact_manager.add_contact(contact)
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            contact_manager.search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()