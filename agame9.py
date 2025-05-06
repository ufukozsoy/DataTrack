import random

def display_intro():
    print("Welcome to the Golf Game!")
    print("Your goal is to get the ball into the hole in as few strokes as possible.")
    print("Let's begin!\n")

def take_shot():
    power = int(input("Enter shot power (1-10): "))
    accuracy = int(input("Enter shot accuracy (1-10): "))
    distance = random.randint(1, 10) * power
    deviation = random.randint(-5, 5) * (10 - accuracy)
    return distance + deviation

def play_game():
    hole_distance = random.randint(50, 150)
    print(f"The hole is {hole_distance} meters away.")
    strokes = 0
    current_distance = 0

    while current_distance < hole_distance:
        strokes += 1
        print(f"\nStroke {strokes}:")
        shot_distance = take_shot()
        current_distance += shot_distance
        print(f"You hit the ball {shot_distance} meters.")
        if current_distance < hole_distance:
            print(f"You are {hole_distance - current_distance} meters away from the hole.")
        elif current_distance > hole_distance:
            print(f"You overshot by {current_distance - hole_distance} meters!")

    print(f"\nCongratulations! You got the ball in the hole in {strokes} strokes.")

if __name__ == "__main__":
    display_intro()
    play_game()