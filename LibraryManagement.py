# Import functions from other modules
from bookoperations import book_operations
from authoroperations import author_operations
from useroperations import user_operations
from genreoperations import genre_operations

def main_menu():
    while True:
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")
        choice = input("Select an option: ")

        if choice == '1':
            book_operations()
        elif choice == '2':
            user_operations()
        elif choice == '3':
            author_operations()
        elif choice == '4':
            genre_operations()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()