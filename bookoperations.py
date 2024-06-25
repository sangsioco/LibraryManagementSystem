from class_book import Book
from genreoperations import genres as genre_list  # Renamed to avoid collision
from useroperations import users  # Import the users list from user_operations
from class_genre import Genre  # Assuming Genre class needs to be imported
import datetime #check if this has been taught yet

books = []
genres = genre_list  # Using renamed import for clarity

def book_operations():
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Reserve a book")
        print("4. Return a book")
        print("5. Search for a book")
        print("6. Display all books")
        print("7. Save books list to text file")
        print("8. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_new_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            reserve_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            search_book()
        elif choice == '6':
            display_all_books()
        elif choice == '7':
            save_book_to_file(books)
            print("Books list saved to file.")
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

def add_new_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    
    while True:
        ISBN = input("Enter book ISBN (13-digit format): ")
        if len(ISBN) == 13 and ISBN.isdigit():
            # Check if ISBN already exists
            existing_book = next((book for book in books if book.get_ISBN() == ISBN), None)
            if existing_book:
                print("ISBN already exists. Please enter another one.")
                continue
            else:
                break
        else:
            print("Invalid ISBN format. Please enter a 13-digit number.")
    
    while True:
        publication_date = input("Enter publication date (YYYY-MM-DD): ")
        try:
        # Attempt to convert the input to a datetime object
            datetime.datetime.strptime(publication_date, '%Y-%m-%d')
        
        # Additional validation for month and day digits
            year, month, day = publication_date.split('-')
            if len(month) != 2 or len(day) != 2:
                raise ValueError  # Raise an error if month or day doesn't have exactly 2 digits
        
            break  # If successful and format is correct, break out of the loop
    
        except ValueError:
            print("Incorrect date format. Please enter the date in YYYY-MM-DD format with two-digit month and day.")
        
    genre_name = input("Enter book genre: ")
    category = input("Enter book category: ")

  # Check if genre exists, otherwise add it
    genre = next((g for g in genres if g.get_name().lower() == genre_name.lower()), None)
    if not genre:
        description = input(f"Enter description for genre '{genre_name}': ")
        genre = Genre(genre_name, description)
        genre.add_category(category)  # Add the initial category to the genre
        genres.append(genre)
    else:
        if category not in genre.get_categories():
            genre.add_category(category)  # Add category to existing genre

    new_book = Book(title, author, ISBN, publication_date, genre_name, category)
    books.append(new_book)
    print(f"Book '{title}' by '{author}' added successfully with genre '{genre_name}' and category '{category}'.")   

def borrow_book():
    title = input("Enter the title of the book to borrow: ")
    author = input("Enter the author of the book to borrow: ")

    found_books = [book for book in books if book.get_title().lower() == title.lower() and book.get_author().lower() == author.lower()]

    if not found_books:
        print(f"No book found with title '{title}' and author '{author}'.")
        return

    if len(found_books) > 1:
        print("Multiple books found with the same title and author. Please select one:")
        for index, book in enumerate(found_books, start=1):
            print(f"{index}. {book.get_title()} by {book.get_author()}")
        choice = input("Enter the number corresponding to the book you want to borrow: ")
        try:
            index = int(choice) - 1
            selected_book = found_books[index]
        except (ValueError, IndexError):
            print("Invalid choice. Returning to main menu.")
            return
    else:
        selected_book = found_books[0]

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    library_id = input("Enter your library ID: ")

    borrow_selected_book(selected_book, first_name, last_name, library_id)

def borrow_selected_book(book, first_name, last_name, library_id):
    found_user = next((user for user in users if user.get_first_name().lower() == first_name.lower() and user.get_last_name().lower() == last_name.lower() and user.get_library_id() == library_id), None)
    
    if found_user:
        if found_user.borrow_book(book):
            print(f"You have borrowed '{book.get_title()}' by {book.get_author()} with ISBN # {book.get_ISBN()}.")
        else:
            print(f"The book '{book.get_title()}' by {book.get_author()} is not available.")
    else:
        print(f"No user found with the provided details. Please try again.")

def reserve_book():
    title = input("Enter the title of the book to reserve: ")
    author = input("Enter the author of the book to reserve: ")

    found_books = [book for book in books if book.get_title().lower() == title.lower() and book.get_author().lower() == author.lower()]

    if not found_books:
        print(f"No book found with title '{title}' and author '{author}'.")
        return

    if len(found_books) > 1:
        print("Multiple books found with the same title and author. Please select one:")
        for index, book in enumerate(found_books, start=1):
            print(f"{index}. {book.get_title()} by {book.get_author()}")
        choice = input("Enter the number corresponding to the book you want to reserve: ")
        try:
            index = int(choice) - 1
            selected_book = found_books[index]
        except (ValueError, IndexError):
            print("Invalid choice. Returning to main menu.")
            return
    else:
        selected_book = found_books[0]

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    library_id = input("Enter your library ID: ")

    found_user = next((user for user in users if user.get_first_name().lower() == first_name.lower() and user.get_last_name().lower() == last_name.lower() and user.get_library_id() == library_id), None)

    if found_user:
        if found_user.reserve_book(selected_book):
            print(f"You have reserved '{selected_book.get_title()}' by {selected_book.get_author()} with ISBN # {selected_book.get_ISBN()}.")
        else:
            print(f"The book '{selected_book.get_title()}' by {selected_book.get_author()} is not available for reservation.")
    else:
        print(f"No user found with the provided details. Please try again.")

def return_book():
    borrowed_books = [book for book in books if not book.is_available()]
    if not borrowed_books:
        print("No book is checked out.")
        return

    ISBN = input("Enter the ISBN of the book to return: ")
    for book in books:
        if book.get_ISBN() == ISBN and not book.is_available():
            found_user = next((user for user in users if ISBN in user.get_borrowed_books()), None)
            if found_user:
                book.return_book()
                found_user.return_book(book)
                print(f"You have returned '{book.get_title()}' by '{book.get_author()}'.")
                return
    print("Book not found or already returned.")

def search_book():
    title = input("Enter the title of the book to search: ")
    for book in books:
        if book.get_title().lower() == title.lower():
            print(f"Book found: {book.get_title()}, Author: {book.get_author()}, ISBN: {book.get_ISBN()}, Availability: {'Available' if book.is_available() else 'Borrowed'}")
            return
    print("Book not found.")

def display_all_books():
    if not books:
        print("No books available.")
    else:
        for book in books:
            status = 'Available' if book.is_available() else 'Borrowed'
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, ISBN: {book.get_ISBN()}, Availability: {status}")

def save_book_to_file(books):
    with open('book_list.txt', 'w') as file:
        for book in books:
            status = 'Available' if book.is_available() else 'Borrowed'
            file.write(f"Title: {book.get_title()}, Author: {book.get_author()}, ISBN: {book.get_ISBN()}, Availability: {status}\n")

