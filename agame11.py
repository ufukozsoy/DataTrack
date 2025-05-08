import time

def intro():
    print("Welcome to the year 3023!")
    print("The Earth is now a hub of advanced technology and intergalactic travel.")
    print("You are a space explorer tasked with a critical mission.")
    print("Your goal is to retrieve a rare energy crystal from a distant planet.")
    print("But beware, the journey is full of challenges and surprises!")
    print()

def choose_path():
    print("You have two paths to choose from:")
    print("1. Take the shortcut through the asteroid field.")
    print("2. Take the longer but safer route around the nebula.")
    choice = input("Which path will you choose? (1/2): ")
    return choice

def asteroid_field():
    print("\nYou enter the asteroid field. It's a dangerous path!")
    time.sleep(2)
    print("An asteroid is heading straight for your ship!")
    action = input("Do you: (a) try to dodge it, or (b) fire your lasers? (a/b): ")
    if action == "a":
        print("\nYou successfully dodge the asteroid and continue your journey!")
        return True
    elif action == "b":
        print("\nYour lasers miss, and the asteroid damages your ship. Mission failed!")
        return False
    else:
        print("\nInvalid choice. The asteroid hits your ship. Mission failed!")
        return False

def nebula_route():
    print("\nYou take the longer route around the nebula.")
    time.sleep(2)
    print("The journey is smooth, but you encounter a pirate ship!")
    action = input("Do you: (a) negotiate with the pirates, or (b) prepare for battle? (a/b): ")
    if action == "a":
        print("\nThe pirates agree to let you pass in exchange for some supplies. You continue your journey!")
        return True
    elif action == "b":
        print("\nThe pirates overpower your ship. Mission failed!")
        return False
    else:
        print("\nInvalid choice. The pirates attack your ship. Mission failed!")
        return False

def main():
    intro()
    path = choose_path()
    if path == "1":
        success = asteroid_field()
    elif path == "2":
        success = nebula_route()
    else:
        print("\nInvalid choice. Your mission ends here.")
        return

    if success:
        print("\nCongratulations! You successfully retrieve the energy crystal and complete your mission!")
    else:
        print("\nBetter luck next time, space explorer!")

if __name__ == "__main__":
    main()