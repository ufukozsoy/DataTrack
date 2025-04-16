import random
import time

def display_intro():
    print("Welcome to the Plastic Pollution Game!")
    print("Your mission is to clean up the ocean by collecting plastic waste.")
    print("Avoid obstacles and collect as much plastic as you can!")
    print("Let's save the environment together!\n")

def get_player_name():
    return input("Enter your name, hero: ")

def display_instructions():
    print("\nInstructions:")
    print("1. Type 'collect' to pick up plastic.")
    print("2. Type 'dodge' to avoid obstacles.")
    print("3. Type 'quit' to exit the game.\n")

def play_game(player_name):
    score = 0
    lives = 4
    actions = ['plastic', 'obstacle']

    print(f"Good luck, {player_name}! The game begins now!\n")
    time.sleep(1)

    while lives > 0:
        action = random.choice(actions)
        print("Something is coming your way!")
        player_action = input("What will you do? (collect/dodge): ").strip().lower()

        if player_action == 'quit':
            print("Thanks for playing!")
            break

        if action == 'plastic' and player_action == 'collect':
            print("You collected plastic! Great job!")
            score += 10
        elif action == 'obstacle' and player_action == 'dodge':
            print("You dodged an obstacle! Well done!")
        elif action == 'plastic' and player_action == 'dodge':
            print("You missed the plastic!")
        elif action == 'obstacle' and player_action == 'collect':
            print("You hit an obstacle! You lost a life.")
            lives -= 1
        else:
            print("Invalid action. Be careful!")

        print(f"Score: {score} | Lives: {lives}\n")
        time.sleep(1)

    if lives == 0:
        print("Game over! You ran out of lives.")
        print(f"Your final score is: {score}")

def main():
    display_intro()
    player_name = get_player_name()
    display_instructions()
    play_game(player_name)

if __name__ == "__main__":
    main()