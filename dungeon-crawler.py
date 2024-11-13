import random
import sys

# Variables
game_playing = True

monster_random = { 
    "escape" : "You have successfully escaped the monster!", 
    "die" : "You lost the fight and died!"
}

crypt = {
    "riddle" : "I slip through the murk, silent and quick, With scales and teeth, sharp and slick. What am I?", 
    "puzzle" : "In a swamp, there are 3 frogs on a lily pad. Each frog catches 2 flies. How many flies are caught in total?", 
    "monster" : "You encounter a Slime! Would you like to run or fight?"
}

crypt_answer = {
    "riddle" : "alligator", 
    "puzzle" : "6"
}

wooded = {
    "riddle" : "I howl at the moon, swift and bold, Through forests deep, both young and old. My eyes gleam bright, in the darkest night.", 
    "puzzle" : "In the depths of the forest, there are 5 trees. Each tree has 6 branches, and each branch has 4 birds. How many birds are in total?", 
    "monster" : "You encounter a Troll! Would you like to run or fight?"
}

wooded_answer = {
    "riddle" : "wolf", 
    "puzzle" : "120"
}

desert = {
    "riddle" : "I store water, though I’m not a well, I live in the heat where no rain dwells. With a spiny crown, I stand so tall, What am I?", 
    "puzzle" : "In a desert, a caravan starts with 64 gallons of water. Each day, they use 8 gallons of water. How many days will the caravan be able to travel before running out of water?", 
    "monster" : "You encounter a Mummy! Would you like to run or fight?"
}

desert_answer = {
    "riddle" : "cactus", 
    "puzzle" : "64"
}

# Player's Name/Intro
name = str(input(f"Hello Brave Adventurer! Please enter your name: "))
print()
players_name = name.capitalize()
print(f"Hello {players_name}! Welcome to Dungeon Crawler! Your goal is to escape three dangerous dungeons ahead of you. Be ready to use your brain, as well as your brawn!")
print()

# Dungeon Choosing
def dungeon_choosing():
    global chosen_dungeon, dungeons_left
    while game_playing:
        chosen_dungeon = input(f"Carefully choose a dungeon from the list - (Crypt Dungeon, Desert Dungeon, or Wooded Dungeon): ").capitalize()
        
        if chosen_dungeon == 'Crypt' or chosen_dungeon == 'Desert' or chosen_dungeon == 'Wooded':
            break
        else:
            print(f"That is not an option. Please type the name of the Dungeon. (Exclude the word Dungeon)")

    if chosen_dungeon == "Crypt":
        dungeons_left = ["Wooded", "Desert"]
    elif chosen_dungeon == "Wooded":
        dungeons_left = ["Crypt", "Desert"]
    elif chosen_dungeon == "Desert":
        dungeons_left = ["Wooded", "Crypt"]

# Dungeon Encounters
def dungeon_encounter(chosen_dungeon):
    global game_playing
    encounter = random.choice(["riddle", "puzzle", "monster"])
    print()

    # Crypt Dungeon Encounter
    if chosen_dungeon == "Crypt":
        if encounter == "riddle": 
            print(crypt["riddle"])
            riddle_answer = input("Be aware but type your answer here: ").lower()
            if riddle_answer == crypt_answer["riddle"]:
                print()
                print("You got it right, let's move on!")
            else:
                print("You got it wrong! Prepare to die!")
                game_playing = False
                sys.exit()
        elif encounter == "puzzle":
            print(crypt["puzzle"])
            puzzle_answer = input("Do you have what it takes to not make mistakes: ")
            if puzzle_answer == crypt_answer["puzzle"]:
                print()
                print("You got it right, let's move on!")
            else:
                print("You got it wrong! Prepare to die!")
                game_playing = False
                sys.exit()
        elif encounter == "monster":
            print(crypt["monster"])
            monster_answer = input("Do you wish to run or fight? ").lower()
            print()
            if monster_answer == "run" or monster_answer == "fight":
                monster_decision = random.choice(list(monster_random.keys()))
                print(monster_random[monster_decision])
                if monster_decision == "die":
                    game_playing = False
                    sys.exit()

    # Wooded Dungeon Encounter
    elif chosen_dungeon == "Wooded":
        if encounter == "riddle": 
            print(wooded["riddle"])
            riddle_answer = input("Be aware but type your answer here: ").lower()
            if riddle_answer == wooded_answer["riddle"]:
                print()
                print("You got it right, let's move on!")
            else:
                print("You got it wrong! Prepare to die!")
                game_playing = False
                sys.exit()
        elif encounter == "puzzle":
            print(wooded["puzzle"])
            puzzle_answer = input("Do you have what it takes to not make mistakes: ")
            if puzzle_answer == wooded_answer["puzzle"]:
                print()
                print("You got it right, let's move on!")
            else:
                print("You got it wrong! Prepare to die!")
                game_playing = False
                sys.exit()
        elif encounter == "monster":
            print(wooded["monster"])
            monster_answer = input("Do you wish to run or fight? ").lower()
            print()
            if monster_answer == "run" or monster_answer == "fight":
                monster_decision = random.choice(list(monster_random.keys()))
                print(monster_random[monster_decision])
                if monster_decision == "die":
                    game_playing = False
                    sys.exit()

    # Desert Dungeon Encounter
    elif chosen_dungeon == "Desert":
        if encounter == "riddle": 
            print(desert["riddle"])
            riddle_answer = input("Be aware but type your answer here: ").lower()
            if riddle_answer == desert_answer["riddle"]:
                print()
                print("You got it right, let's move on!")
            else:
                print("You got it wrong! Prepare to die!")
                game_playing = False
                sys.exit()
        elif encounter == "puzzle":
            print(desert["puzzle"])
            puzzle_answer = input("Do you have what it takes to not make mistakes: ")
            if puzzle_answer == desert_answer["puzzle"]:
                print()
                print("You got it right, let's move on!")
            else:
                print("You got it wrong! Prepare to die!")
                game_playing = False
                sys.exit()
        elif encounter == "monster":
            print(desert["monster"])
            monster_answer = input("Do you wish to run or fight? ").lower()
            print()
            if monster_answer == "run" or monster_answer == "fight":
                monster_decision = random.choice(list(monster_random.keys()))
                print(monster_random[monster_decision])
                if monster_decision == "die":
                    game_playing = False
                    sys.exit()

# Makes the Functions Run/Makes Game Run
def play_game():
    global game_playing
    dungeon_choosing()  
    
    # First Dungeon
    print(f"\nEntering {chosen_dungeon} Dungeon!")
    dungeon_encounter(chosen_dungeon)

    # Second Dungeon
    next_dungeon = dungeons_left[0]
    print(f"\nEntering {next_dungeon} Dungeon!")
    dungeon_encounter(next_dungeon)

    # Final Dungeon
    final_dungeon = dungeons_left[1]
    print(f"\nEntering {final_dungeon} Dungeon!")
    dungeon_encounter(final_dungeon)

    # Game Winning or Ending
    if game_playing:
        print()
        print("Congratulations, you have escaped all three dungeons!")
    else:
        print()
        print("Game Over")

# Start the Game
play_game()