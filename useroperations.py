from class_user import User

users = []

def user_operations():
    while True:
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Save users list to txt file")
        print("5. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_new_user()
        elif choice == '2':
            view_user_details()
        elif choice == '3':
            display_all_users()
        elif choice == '4':
            save_user_to_file(users)
            print("Users list saved to file.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_new_user():
    first_name = input("Enter user first name: ")
    last_name = input("Enter user last name: ")
    while True:
        library_id = input("Enter user library ID: ")

        if any(user.get_library_id() == library_id for user in users):
            print("Library ID already exists. Please enter a different one.")
            continue
        else:
            break

    new_user = User(first_name, last_name, library_id)
    users.append(new_user)
    print(f"User '{new_user.get_name()}' added successfully.")

def view_user_details():
    library_id = input("Enter user library ID: ")
    for user in users:
        if user.get_library_id() == library_id:
            borrowed_books = user.get_borrowed_books()
            borrowed_books_display = ', '.join(borrowed_books) if borrowed_books else 'None'
            print(f"User found: {user.get_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {borrowed_books_display}")
            return
    print("User not found with that library id.")

def display_all_users():
    if not users:
        print("No users available.")
    for user in users:
        borrowed_books = user.get_borrowed_books()
        borrowed_books_display = ', '.join(borrowed_books) if borrowed_books else 'None'
        print(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {borrowed_books_display}")

def save_user_to_file(users):
    with open('user_list.txt', 'w') as file:
        for user in users:
            borrowed_books = user.get_borrowed_books()
            borrowed_books_display = ', '.join(borrowed_books) if borrowed_books else 'None'
            file.write(f"Name: {user.get_name()}, Library ID: {user.get_library_id()}, Borrowed Books: {borrowed_books_display}\n")
