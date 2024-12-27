import csv
import os

# Path to the contacts file
CONTACTS_FILE = "contacts.csv"

# Ensure the file exists
if not os.path.exists(CONTACTS_FILE):
    with open(CONTACTS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])  # Header row


def add_contact(name, phone, email):
    """Add a new contact to the CSV file."""
    with open(CONTACTS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print(f"Contact '{name}' added successfully!")


def search_contact(name):
    """Search for a contact by name."""
    found = False
    with open(CONTACTS_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if name.lower() in row[0].lower():
                print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
                found = True
    if not found:
        print(f"No contact found with the name '{name}'.")


def delete_contact(name):
    """Delete a contact by name."""
    found = False
    with open(CONTACTS_FILE, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
    with open(CONTACTS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            if row and name.lower() != row[0].lower():
                writer.writerow(row)
            else:
                found = True
    if found:
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"No contact found with the name '{name}'.")


def list_contacts():
    """List all contacts."""
    with open(CONTACTS_FILE, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        if len(rows) <= 1:
            print("No contacts available.")
        else:
            print("Contacts:")
            for row in sorted(rows[1:]):  # Skip header, sort alphabetically
                print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")


def main():
    """Main function to display the menu and handle user input."""
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. List All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            add_contact(name, phone, email)
        elif choice == "2":
            name = input("Enter Name to Search: ")
            search_contact(name)
        elif choice == "3":
            name = input("Enter Name to Delete: ")
            delete_contact(name)
        elif choice == "4":
            list_contacts()
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
