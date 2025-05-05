import random

def movie_guessing_game():
    movies = [
        "Inception", "Titanic", "Avatar", "The Matrix", "The Godfather",
        "Pulp Fiction", "The Dark Knight", "Forrest Gump", "Gladiator", "Interstellar"
    ]
    selected_movie = random.choice(movies).lower()
    hidden_movie = ["_" if char.isalpha() else char for char in selected_movie]
    attempts = 6

    print("Welcome to the Movie Guessing Game!")
    print("Guess the movie title one letter at a time.")
    print("You have 6 incorrect attempts. Good luck!\n")

    while attempts > 0 and "_" in hidden_movie:
        print("Movie: " + " ".join(hidden_movie))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in selected_movie:
            for i, char in enumerate(selected_movie):
                if char == guess:
                    hidden_movie[i] = guess
            print("Correct!")
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")

    if "_" not in hidden_movie:
        print("\nCongratulations! You guessed the movie:", selected_movie.title())
    else:
        print("\nGame Over! The movie was:", selected_movie.title())

if __name__ == "__main__":
    movie_guessing_game()