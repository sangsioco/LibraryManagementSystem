from class_genre import Genre  # Import the Genre class

genres = []

def genre_operations():
    while True:
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")
        print("4. Save genres list to txt file")
        print("5. Return to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            add_new_genre()
        elif choice == '2':
            view_genre_details()
        elif choice == '3':
            display_all_genres()
        elif choice == '4':
            save_genre_to_file(genres)
            print("Authors list saved to file.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_new_genre():
    name = input("Enter genre name: ")
    description = input("Enter genre description: ")
    category = input("Enter genre category: ")

    # Check if genre already exists
    existing_genre = get_genre_by_name(name)
    if existing_genre:
        print(f"Genre '{name}' already exists.")
        return

    # Create new Genre object and add to genres list
    new_genre = Genre(name, description)
    new_genre.add_category(category)
    genres.append(new_genre)
    print(f"Genre '{name}' added successfully.")

def get_genre_by_name(name):
    for genre in genres:
        if genre.get_name().lower() == name.lower():
            return genre
    return None

def view_genre_details():
    name = input("Enter genre name: ")
    genre = get_genre_by_name(name)
    if genre:
        print(f"Genre found: {genre.get_name()}, Description: {genre.get_description()}, Categories: {genre.get_categories()}")
    else:
        print("Genre not found.")

def display_all_genres():
    if not genres:
        print("No genres available.")
    else:
        for genre in genres:
            print(f"Name: {genre.get_name()}, Description: {genre.get_description()}, Categories: {genre.get_categories()}")

def save_genre_to_file(genres):
    with open('genre_list.txt', 'w') as file:
        for genre in genres:
            file.write(f"Name: {genre.get_name()}, Description: {genre.get_description()}, Categories: {genre.get_categories()}")

