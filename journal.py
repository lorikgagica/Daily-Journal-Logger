# Daily Journal Logger

from datetime import datetime

# Step 1: Define the journal file
JOURNAL_FILE = 'daily_journal.txt'

# Step 2: Add a new entry
def add_entry():
    entry = input("Write your journal entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(JOURNAL_FILE, 'a', encoding="utf-8") as file:
        file.write(f"[{timestamp}] {entry}\n")
    print("Entry added successfully!")

# Step 3: View all entries
def view_entries():
    try:
        with open(JOURNAL_FILE, 'r', encoding="utf-8") as file:
            content = file.readlines()
            if content:
                print("\n--- Your Journal Entries ---")
                for idx, entry in enumerate(content, 1):
                    print(f"{idx}. {entry.strip()}")
            else:
                print("No entries found. Start writing today.")
    except FileNotFoundError:
        print("No journal file found. Add an entry first!")

# Step 4: Search entries by keyword
def search_entries():
    keyword = input("Enter a keyword to search for: ").lower()
    try:
        with open(JOURNAL_FILE, 'r', encoding="utf-8") as file:
            content = file.readlines()
            found = False
            print("\n--- Search Results ---")
            for entry in content:
                if keyword in entry.lower():
                    print(entry.strip())
                    found = True
            if not found:
                print("No matching entries found.")
    except FileNotFoundError:
        print("No journal file found. Add an entry first!")

# Step 5: Delete an entry
def delete_entry():
    try:
        with open(JOURNAL_FILE, 'r', encoding="utf-8") as file:
            entries = file.readlines()
        if not entries:
            print("No entries to delete.")
            return
        view_entries()
        num = int(input("Enter the entry number to delete: "))
        if 1 <= num <= len(entries):
            entries.pop(num - 1)
            with open(JOURNAL_FILE, 'w', encoding="utf-8") as file:
                for entry in entries:
                    file.write(entry)
            print("Entry deleted successfully!")
        else:
            print("Invalid entry number.")
    except (FileNotFoundError, ValueError):
        print("Delete failed. Check entry number and file.")

# Step 6: Modify an entry
def modify_entry():
    try:
        with open(JOURNAL_FILE, 'r', encoding="utf-8") as file:
            entries = file.readlines()
        if not entries:
            print("No entries to modify.")
            return
        view_entries()
        num = int(input("Enter the entry number to modify: "))
        if 1 <= num <= len(entries):
            new_entry = input("Write your new entry for this position: ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entries[num - 1] = f"[{timestamp}] {new_entry}\n"
            with open(JOURNAL_FILE, 'w', encoding="utf-8") as file:
                for entry in entries:
                    file.write(entry)
            print("Entry modified successfully!")
        else:
            print("Invalid entry number.")
    except (FileNotFoundError, ValueError):
        print("Modification failed. Check entry number and file.")

# Step 7: Display Menu
def show_menu():
    print("\n--- Daily Journal Logger ---")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search entries by keyword")
    print("4. Delete an entry")
    print("5. Modify an entry")
    print("6. Exit")

# Step 8: Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ").strip()
    if choice == '1':
        add_entry()
    elif choice == '2':
        view_entries()
    elif choice == '3':
        search_entries()
    elif choice == '4':
        delete_entry()
    elif choice == '5':
        modify_entry()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")