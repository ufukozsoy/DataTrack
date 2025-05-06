import random

def tv_series_game():
    series_list = [
        "Breaking Bad",
        "Game of Thrones",
        "Stranger Things",
        "The Office",
        "Friends",
        "The Mandalorian",
        "Sherlock",
        "The Crown",
        "The Witcher",
        "Better Call Sal"
    ]

    print("Welcome to the TV Series Guessing Game!")
    print("Try to guess the TV series name. You have 3 attempts.")

    selected_series = random.choice(series_list).lower()
    attempts = 3

    while attempts > 0:
        guess = input("Enter your guess: ").lower()
        if guess == selected_series:
            print("Congratulations! You guessed it right!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong guess. Try again! Attempts left: {attempts}")
            else:
                print(f"Game over! The correct answer was: {selected_series}")

if __name__ == "__main__":
    tv_series_game()