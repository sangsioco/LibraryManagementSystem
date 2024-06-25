from class_author import Author

authors = []

def author_operations():
    while True:
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Save authors list to txt file")
        print("5. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_new_author()
        elif choice == '2':
            view_author_details()
        elif choice == '3':
            display_all_authors()
        elif choice == '4':
            save_author_to_file(authors)
            print("Authors list saved to file.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_new_author():
    first_name = input("Enter author first name: ")
    last_name = input("Enter author last name: ")
    biography = input("Enter author biography: ")
    new_author = Author(first_name, last_name, biography)
    authors.append(new_author)
    print(f"Author '{new_author.get_name()}' added successfully.")

def view_author_details():
    last_name = input("Enter author's last name: ")
    matching_authors = [author for author in authors if author.get_last_name().lower() == last_name.lower()]
    
    if matching_authors:
        if len(matching_authors) > 1:
            print("Multiple authors found with the last name. Please select one:")
            for index, author in enumerate(matching_authors, start=1):
                print(f"{index}. {author.get_name()}")
            choice = input("Enter the number corresponding to the author: ")
            try:
                index = int(choice) - 1
                selected_author = matching_authors[index]
                print(f"Author found: {selected_author.get_name()}, Biography: {selected_author.get_biography()}")
            except (ValueError, IndexError):
                print("Invalid choice.")
        else:
            selected_author = matching_authors[0]
            print(f"Author found: {selected_author.get_name()}, Biography: {selected_author.get_biography()}")
    else:
        print("Author not found.")

def display_all_authors():
    if not authors:
        print("No authors available.")
    else:
        for author in authors:
            print(f"Name: {author.get_name()}, Biography: {author.get_biography()}")

def save_author_to_file(authors):
    with open('author_list.txt', 'w') as file:
        for author in authors:
            file.write(f"{author.get_first_name()} {author.get_last_name()}\n")

