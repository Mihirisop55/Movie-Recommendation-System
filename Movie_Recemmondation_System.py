# Movie Recommendation System

genres = ["1. Anime", "2. Action / Adventure", "3. Comedy", "4. Drama", "5. Horror", "6. Romance", "7. Sci-Fi / Fantasy", "8. Thriller / Mystery"]

short_movies = {"Anime": ["Your Name", "A Silent Voice", "Spirited Away"],
         "Action / Adventure": ["Kung Fury", "Run Lola Run", "District B13"],
         "Comedy": ["The Music Box", "Six Shooter", "The Accountant"],
         "Drama": ["Sing", "Hotel Chevalier", "Timecode"],
         "Horror": ["Lights Out", "The Strange Thing About the Johnsons", "Zygote"],
         "Romance": ["Paperman", "The Lunch Date", "Lift"],
         "Sci-Fi / Fantasy": ["The Black Hole", "A Single Life", "Curfew"],
         "Thriller / Mystery": ["Duel", "The Phone Call", "Whiplash"]}

long_movies = {"Anime": ["The Girl Who Leapt Through Time", "The Tale of the Princess Kaguya", "Perfect Blue"],
               "Action / Adventure": ["The Lord of the Rings: The Return of the King", "Lawrence of Arabia", "Ran"],
               "Comedy": ["It's a Mad, Mad, Mad, Mad World", "The Wolf of Wall Street"],
               "Drama": ["Resan (The Journey)", "La flor", "Out 1"],
               "Horror": ["Grindhouse", "Kwaidan", "The Wailing"],
               "Romance": ["Mera Naam Joker", "LOC Kargil"],
               "Sci-Fi / Fantasy": ["Dune: Part Two", "The Lord of the Rings: The Two Towers", "Avatar: The Way of Water"],
               "Thriller / Mystery": ["Oppenheimer", "Killers of the Flower Moon", "The Irishman"]}

print("------------------------------------------------")
print("Welcome to the Movie Recommendation System!")
print("Please select a genre from the following list:")
for i in genres:
    print(i)
print("------------------------------------------------")
running = True
while running:
    choice = input("Enter the number corresponding to your choice (or 'q' to quit): ")
    if choice.isalpha():
        if choice.lower() == 'q':
            print("Thank you for using the Movie Recommendation System. Goodbye!")
            running = False
        else:
            print("Invalid input. Please enter 'q' to quit.")
            continue
    elif choice.isdigit():
        choice = int(choice)
        if choice < 1 or choice > 8:
            print("Invalid choice. Please select a number between 1 and 8 (or 'q' to quit).")
            continue
        elif choice >= 1 and choice < 9:
            length = input("Do you want to watch a short movie or a long movie? (Enter 'short' or 'long'): ")
            if length.isdigit():
                print("Invalid input. Please enter 'short' or 'long'.")
                continue
            elif length.lower() != "short" and length.lower() != "long":
                print("Invalid input. Please enter 'short' or 'long'.")
                continue
            elif length.isalpha():
                if length.lower() == "short":
                    genre = genres[choice - 1].split(". ")[1]
                    print(f"Here are some short {genre} movies you might enjoy:")
                    short_list = short_movies[genre]
                    for m in short_list:
                        print(f"- {m}")
                elif length.lower() == "long":
                    genre = genres[choice - 1].split(". ")[1]
                    print(f"Here are some long {genre} movies you might enjoy:")
                    long_list = long_movies[genre]
                    for m in long_list:
                        print(f"- {m}")
