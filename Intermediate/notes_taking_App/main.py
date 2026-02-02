import os
FILE_NAME = os.path.join(os.getcwd(), "notes.txt")  # Get the current working directory and join it with the filename

def display():
    print("\n===== Notes Taking App =====")
    print("1. Add New Note")
    print("2. View All Notes")
    print("3. Search A Note")
    print("4. Update A Note")
    print("5. Delete A Note")
    print("6. Exit")

def get_next_id():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()
            if not lines:
                return 1
            last_line = lines[-1]
            return int(last_line.split("|")[0]) + 1
    except FileNotFoundError:
        return 1

def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")

    note_id = get_next_id()

    with open(FILE_NAME, "a") as file:
        file.write(f"{note_id}|{title}|{content}\n")

    print("✅ Note added successfully!")

def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()
            if not notes:
                print("No notes found.")
                return

            for note in notes:
                note_id, title, content = note.strip().split("|")
                print(f"\nID: {note_id}")
                print(f"Title: {title}")
                print(f"Content: {content}")
    except FileNotFoundError:
        print("No notes file found.")

def search_note():
    keyword = input("Enter title keyword to search: ").lower()
    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for note in file:
                note_id, title, content = note.strip().split("|")
                if keyword in title.lower():
                    print(f"\nID: {note_id}")
                    print(f"Title: {title}")
                    print(f"Content: {content}")
                    found = True

        if not found:
            print("❌ No matching note found.")
    except FileNotFoundError:
        print("No notes file found.")

def update_note():
    note_id_to_update = input("Enter note ID to update: ")
    updated_lines = []
    updated = False

    try:
        with open(FILE_NAME, "r") as file:
            for note in file:
                note_id, title, content = note.strip().split("|")
                if note_id == note_id_to_update:
                    new_title = input("Enter new title: ")
                    new_content = input("Enter new content: ")
                    updated_lines.append(f"{note_id}|{new_title}|{new_content}\n")
                    updated = True
                else:
                    updated_lines.append(note)

        if updated:
            with open(FILE_NAME, "w") as file:
                file.writelines(updated_lines)
            print("✅ Note updated successfully!")
        else:
            print("❌ Note ID not found.")
    except FileNotFoundError:
        print("No notes file found.")

def delete_note():
    note_id_to_delete = input("Enter note ID to delete: ")
    remaining_notes = []
    deleted = False

    try:
        with open(FILE_NAME, "r") as file:
            for note in file:
                note_id, _, _ = note.strip().split("|")
                if note_id != note_id_to_delete:
                    remaining_notes.append(note)
                else:
                    deleted = True

        if deleted:
            with open(FILE_NAME, "w") as file:
                file.writelines(remaining_notes)
            print("🗑️ Note deleted successfully!")
        else:
            print("❌ Note ID not found.")
    except FileNotFoundError:
        print("No notes file found.")

def main():
    while True:
        display()
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_note()
            elif choice == 2:
                view_notes()
            elif choice == 3:
                search_note()
            elif choice == 4:
                update_note()
            elif choice == 5:
                delete_note()
            elif choice == 6:
                print("👋 Exiting app. Bye!")
                break
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

if __name__ == "__main__":
    main()
