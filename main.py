class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        contact = Contact(name, number)
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully.")

    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Contact found: {contact.name} - {contact.number}")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{contact.name}' deleted successfully.")
                return
        print("Contact not found.")

    def display_contacts(self):
        if not self.contacts:
            print("Phone book is empty.")
            return
        print("Contacts:")
        for contact in self.contacts:
            print(f"{contact.name} - {contact.number}")

# Main
def main():
    phone_book = PhoneBook()

    while True:
        print("\n--- Phone Book ---")
        print("1. Add contact")
        print("2. Find contact")
        print("3. Delete contact")
        print("4. Display all contacts")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter number: ")
            phone_book.add_contact(name, number)
        elif choice == "2":
            name = input("Enter name to find: ")
            phone_book.find_contact(name)
        elif choice == "3":
            name = input("Enter name to delete: ")
            phone_book.delete_contact(name)
        elif choice == "4":
            phone_book.display_contacts()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





    