import time

import random

dragons = ["ice_dragon", "fire_dragon", "lightning_dragon"]

dragon = random.choice(dragons)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You have been summoned on a great adventure.")
    print_pause("Your quest is to defeat one of the terrible dragons "
                "that have been menacing our great land.")
    print_pause("You embark from the midst of "
                "a rolling field of verdant "
                "grass, trees, and flowers.")
    print_pause("To your east is a vast cave.")
    print_pause("To your west is an ancient temple.")
    print_pause("To your south is a deep lake.")
    print_pause("To your north is a daunting mountain.")


def choose_dragon(dragon):
    if dragon == "ice_dragon":
        print_pause("A shiver runs through you as the "
                    "air rapidly chills.")
        print_pause("A hulking dragon "
                    "made of glittering blue ice appears!")
        print_pause("He roars and breathes a blast of "
                    "deadly frigid air swiftly toward you.")
    elif dragon == "fire_dragon":
        print_pause("You break out in sweat as your skin "
                    "begins to burn and tingle.")
        print_pause("A towering dragon made of "
                    "crackling red fire appears!")
        print_pause("She roars and breathes a blast of "
                    "scorching heat swiftly toward you.")
    elif dragon == "lightning_dragon":
        print_pause("A fierce gale of wind sweeps around you, "
                    "and the air cracks like a whip.")
        print_pause("An enormous purple dragon surrounded "
                    "by furious storm clouds appears!")
        print_pause("He roars and shoots a blast of "
                    "lethal lightning swiftly toward you.")


def fight_or_flight(items):
    choice = input("1. Fight\n"
                   "2. Run \n")
    if choice == '1':
        if dragon == "ice_dragon":
            if "fire_sword" in items:
                print_pause("You brandish your flaming "
                            "sword and the dragon evaporates, "
                            "spraying you with a fine mist.")
                print_pause("You are victorious!")
            else:
                print_pause("You are no match for this dragon with "
                            "your current arsenal! "
                            "You are defeated!")
        elif dragon == "fire_dragon":
            if "water_spell" in items:
                print_pause("You recite a spell and summon "
                            "mighty waves of water which crash "
                            "toward the dragon, quenching the flames "
                            "which surround her.")
                print_pause("She collapses into "
                            "a pile of grey ash.")
                print_pause("You are victorious!")
            else:
                print_pause("You are no match for this dragon with "
                            "your current arsenal! "
                            "You are defeated!")
        elif dragon == "lightning_dragon":
            if "storm_shield" in items:
                print_pause("Your shield repels the lightning, "
                            "hurling it back at the great dragon.")
                print_pause("The dragon shudders and howls, "
                            "and the clouds disperse. A wind carries "
                            "away the dragon's disintegrating form.")
                print_pause("You are victorious!")
            else:
                print_pause("You are no match for this dragon with "
                            "your current arsenal! "
                            "You are defeated!")
    elif choice == '2':
        print_pause("You escape just in "
                    "the nick of time!")
        field(items)
    else:
        print_pause("Please make a selection of 1 or 2.")
        print_pause("Do you stay and fight, "
                    "or do you run for the hills?")
        fight_or_flight(items)


def cave(items):
    print_pause("After a journey of many miles, you reach "
                "the entrance to a mysterious cave.")
    choose_dragon(dragon)
    print_pause("Do you stay and fight, "
                "or do you run for the hills?")
    print_pause("Please enter a number to choose whether "
                "to fight or run:")
    fight_or_flight(items)


def temple(items):
    print_pause("After a journey of many miles, you reach "
                "the entrance to a great temple.")
    print_pause("The shadowy halls are lit throughout "
                "with stone figures bearing blazing torches.")
    if "fire_sword" not in items:
        print_pause("Inside the temple, the torch fires "
                    "assemble into a spirit "
                    "who gazes at you as flames dance "
                    "around his hovering form.")
        print_pause("He bestows to you "
                    "a gleaming sword enveloped "
                    "in a magical wreath of flame.")
        items.append("fire_sword")
        field(items)
    else:
        print_pause("You have already found "
                    "what you needed here.")
        field(items)


def lake(items):
    print_pause("After a journey of many miles, you reach "
                "the shores of a tranquil lake.")
    print_pause("You feel at peace here, but "
                "know you cannot linger long.")
    if "water_spell" not in items:
        print_pause("A breeze ripples across the lake "
                    "and a spirit made of the purest "
                    "lake water appears.")
        print_pause("She teaches you a spell to summon "
                    "fearsome waves of water at your command.")
        items.append("water_spell")
        field(items)
    else:
        print_pause("You have already found "
                    "what you needed here.")
        field(items)


def mountain(items):
    print_pause("After a journey of many miles, you reach "
                "the foot of a formidable mountain "
                "whose peak pierces beyond the clouds.")
    print_pause("You make the arduous climb to the summit.")
    if "storm_shield" not in items:
        print_pause("A gust of wind passes over you.")
        print_pause("A spirit of clouds and mist "
                    "gathers itself and appears before you.")
        print_pause("He sends aloft a breeze to you a "
                    "tremendous shield.")
        print_pause("It is adorned with a violet mirror "
                    "at its center, and edges and handles made "
                    "of glimmering silver.")
        items.append("storm_shield")
        field(items)
    else:
        print_pause("You have already found "
                    "what you needed here.")
        field(items)


def field(items):
    print_pause("Where would you like to go?")
    print_pause("Please enter the number for the place "
                "you would like to visit:")
    where = input("1. Cave of Unknown Perils\n"
                  "2. Temple of Transforming Flame\n"
                  "3. Lake of Forgetting\n"
                  "4. Skypeak Mountain\n")
    if where == '1':
        cave(items)
    elif where == '2':
        temple(items)
    elif where == '3':
        lake(items)
    elif where == '4':
        mountain(items)
    else:
        print_pause("Please make a selection of 1, 2, 3, or 4.")
        field(items)


def play_again():
    print_pause("Woud you like to play again?")
    print_pause("Please enter 1 for Yes or 2 for No.")
    choice = input("1. Yes\n"
                   "2. No\n")
    if choice == '1':
        global dragon
        dragon = random.choice(dragons)
        dragon_game()
    elif choice == '2':
        print_pause("Thanks for playing! "
                    "See you next time!")
    else:
        print_pause("Sorry, I don't understand.")
        play_again()


def dragon_game():
    items = []
    intro()
    field(items)
    play_again()


dragon_game()
