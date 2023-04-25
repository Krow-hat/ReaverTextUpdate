import sys
import time


def wait_for_user(message):
    print(message)


wait_for_user("Crowhat Studio Presents")
logo = """
 _______  _______  _______           _______  _______ 
(  ____ )(  ____ \(  ___  )|\     /|(  ____ \(  ____ )
| (    )|| (    \/| (   ) || )   ( || (    \/| (    )|
| (____)|| (__    | (___) || |   | || (__    | (____)|
|     __)|  __)   |  ___  |( (   ) )|  __)   |     __)
| (\ (   | (      | (   ) | \ \_/ / | (      | (\ (   
| ) \ \__| (____/\| )   ( |  \   /  | (____/\| ) \ \__
|/   \__/(_______/|/     \|   \_/   (_______/|/   \__/

"""
print(logo)

# game start
input("Enter to continue")
time.sleep(0.3)
print("Welcome to Reaver!")
print()
print()
print()

# character customization
player_name = input("What is your name?: ")
wait_for_user(f"Greetings: {player_name}")
print("Gender has no bearing on ability")
player_gender = input("What is your gender?: ")
wait_for_user("You are a " + player_gender)
time.sleep(0.3)
print()

# game loop
playing = True
while playing:
    # initial choice
    choice = input(
        "You wake up on a deserted beach. You see wreckage from your ship. Do you search for a weapon or leave the beach? Type 'weapon' or 'leave' and press enter: ")

    # first path
    if choice.lower() == "weapon":
        print("You search around the wreckage and find a sword and a wooden shield.")
        print("You continue forward, leaving the beach. ")
        print("You continue forward, you see two goblins sitting about. Do you wish to attack or sneak past?")
        attack_choice = input("Type 'attack' or 'stealth' and press enter: ")
        if attack_choice.lower() == "attack":
            print("You charge towards the goblins, your sword and shield at the ready!")
            print("You easily defeat the goblins and continue on your adventure!")
        elif attack_choice.lower() == "stealth":
            print("You sneak past the goblins without them noticing you!")
            print("You continue on your adventure, avoiding any further confrontations.")
        else:
            print("Invalid input. Please type 'attack' or 'stealth' and press enter.")

        # go to the horse_dead prompt
        horse_dead = input("You find a dead horse, do you wish to loot it or no?")
        if horse_dead.lower() == "loot":
            print("You loot the dead horse, you find 5x potion--------nnnn----!!#$$@#$@$@$@$@ZXCAWEWEWEEQW,")
            time.sleep(0.5)
            print(
                "It seems the simulation crashed, your adventure is over or the creator is too lazy to continue this.")
            break  # exit game loop
        elif horse_dead.lower() == "no":
            print("""Simulation has died
                     Reason: creator too lazy""")
