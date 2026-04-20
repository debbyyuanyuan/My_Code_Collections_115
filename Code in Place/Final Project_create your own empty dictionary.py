#create an empty dictionary
dialect_dict = {}

def main():
    print("\nThis is a dialect dictionary. Please choose whether you want to add a dialect and its meaning into the dictionary, or you can also search up for a dialect you want to know about!")

    # Function to add a word
    def add_word(dialect, meaning):
        dialect_dict[dialect.lower()] = meaning
        print(f"Added: {dialect} → {meaning}")

    # Function to search a word
    def search_word(dialect):
        meaning = dialect_dict.get(dialect.lower())
        if meaning:
            print(f"{dialect} means: {meaning}")
        else:
            print(f"'{dialect}' not found in the dictionary.")

    # Function to view all words
    def view_all():
        if not dialect_dict:
            print("The dictionary is empty.")
        else:
            for word, meaning in dialect_dict.items():
                print(f"{word} → {meaning}")

    # Main menu loop
    while True:
        print("\n1. Add Word\n2. Search Word\n3. View All\n4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            word = input("Enter dialect word: ")
            meaning = input("Enter meaning: ")
            add_word(word, meaning)
        elif choice == '2':
            word = input("Enter word to search: ")
            search_word(word)
        elif choice == '3':
            view_all()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()