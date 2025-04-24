import random

def cricket_game():
    print("Welcome to the Cricket Game!")
    print("You will bat first. Try to score as many runs as possible.")
    
    player_score = 0
    while True:
        try:
            player_choice = int(input("Enter your run (1-6): "))
            if player_choice < 1 or player_choice > 6:
                print("Invalid input! Please enter a number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        computer_choice = random.randint(1, 9)
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("You're out!")
            break
        else:
            player_score += player_choice
            print(f"Your current score: {player_score}")
    
    print(f"Your final score: {player_score}")
    print("Now it's the computer's turn to bat. Try to bowl them out!")
    
    computer_score = 0
    while computer_score <= player_score:
        try:
            player_choice = int(input("Enter your bowl (1-6): "))
            if player_choice < 1 or player_choice > 6:
                print("Invalid input! Please enter a number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        computer_choice = random.randint(1, 6)
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            print("You got the computer out!")
            break
        else:
            computer_score += computer_choice
            print(f"Computer's current score: {computer_score}")
    
    print(f"Computer's final score: {computer_score}")
    
    if player_score > computer_score:
        print("Congratulations! You win!")
    elif player_score < computer_score:
        print("Computer wins! Better luck next time.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    cricket_game()