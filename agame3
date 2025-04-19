import random

class BasketballGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.player_score = 0
        self.opponent_score = 0

    def shoot_ball(self):
        print("\nYou take a shot...")
        if random.random() > 0.5:  # 50% chance to score
            print("It's a score!")
            self.player_score += 2
        else:
            print("You missed!")

    def opponent_turn(self):
        print("\nOpponent takes a shot...")
        if random.random() > 0.5:  # 50% chance to score
            print("Opponent scores!")
            self.opponent_score += 2
        else:
            print("Opponent missed!")

    def display_score(self):
        print(f"\nScoreboard:\n{self.player_name}: {self.player_score} | Opponent: {self.opponent_score}")

    def play(self):
        print(f"Welcome to the basketball game, {self.player_name}!")
        print("First to 10 points wins!")
        
        while self.player_score < 10 and self.opponent_score < 10:
            self.shoot_ball()
            self.opponent_turn()
            self.display_score()

        if self.player_score >= 10:
            print(f"\nCongratulations, {self.player_name}! You won!")
        else:
            print("\nYou lost! Better luck next time.")

if __name__ == "__main__":
    name = input("Enter your name: ")
    game = BasketballGame(name)
    game.play()