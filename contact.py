# contact_book.py
# A simple Contact Book that saves, searches, and deletes contacts
# using a plain text file (contacts.txt). Beginner-friendly version:
# only basic file handling, loops, functions, and if/else are used.

FILE_NAME = "contacts.txt"


def add_contact():
    """Ask the user for details and save them as one line in the file."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    # Each contact is stored as: name,phone,email
    with open(FILE_NAME, "a") as file:
        file.write(name + "," + phone + "," + email + "\n")

    print("Contact saved successfully!\n")


def view_contacts():
    """Read the file and print every contact in a readable format."""
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No contacts saved yet.\n")
        return

    if len(lines) == 0:
        print("Contact list is empty.\n")
        return

    print("\n----- ALL CONTACTS -----")
    count = 1
    for line in lines:
        parts = line.strip().split(",")
        name = parts[0]
        phone = parts[1]
        email = parts[2]
        print(f"{count}. Name: {name} | Phone: {phone} | Email: {email}")
        count = count + 1
    print("-------------------------\n")


def search_contact():
    """Ask for a name and show matching contacts."""
    search_name = input("Enter name to search: ").strip().lower()

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No contacts saved yet.\n")
        return

    found = False
    for line in lines:
        parts = line.strip().split(",")
        name = parts[0]
        phone = parts[1]
        email = parts[2]

        if search_name in name.lower():
            print(f"Found -> Name: {name} | Phone: {phone} | Email: {email}")
            found = True

    if not found:
        print("No contact found with that name.")
    print()


def delete_contact():
    """Ask for a name and remove that contact from the file."""
    delete_name = input("Enter name to delete: ").strip().lower()

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("No contacts saved yet.\n")
        return

    new_lines = []
    deleted = False

    for line in lines:
        parts = line.strip().split(",")
        name = parts[0]

        if name.lower() == delete_name:
            deleted = True  # skip this line, so it gets removed
        else:
            new_lines.append(line)

    # Rewrite the file with the contact removed
    with open(FILE_NAME, "w") as file:
        file.writelines(new_lines)

    if deleted:
        print("Contact deleted successfully!\n")
    else:
        print("No contact found with that name.\n")


def show_menu():
    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()