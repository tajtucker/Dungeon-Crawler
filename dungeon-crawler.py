import random
import sys
#Varaibles
game_playing = True

crypt = {"riddle" : "I slip through the murk, silent and quick, With scales and teeth, sharp and slick. What am I?" , 
"puzzle" : "In a swamp, there are 3 frogs on a lily pad. Each frog catches 2 flies. How many flies are caught in total?" ,
"monster" : "You encounter a Slime! Would you like to run or fight?"
}

crypt_answer = {"riddle" : "alligator" ,
"puzzle" : "6" ,
}

wooded = {"riddle" : "I howl at the moon, swift and bold, Through forests deep, both young and old. My eyes gleam bright, in the darkest night." ,
"puzzle" : "In the depths of the forest, there are 5 trees. Each tree has 6 branches, and each branch has 4 birds. How many birds are in total?" ,
"monster" : "You encounter a Troll! Would you like to run or fight?"
}

wooded_answer = {"riddle" : "wolf" ,
"puzzle" : "120"
}

desert = {"riddle" : "I store water, though I’m not a well, I live in the heat where no rain dwells. With a spiny crown, I stand so tall, What am I?" ,
"puzzle" : "In a desert, a caravan starts with 64 gallons of water. Each day, they use 8 gallons of water. How many days will the caravan be able to travel before running out of water?" ,
"monster" : "You encounter a Mummy! Would you like to run or fight?"
}

desert_answer = {"riddle" : "cactus" ,
"puzzle" : "64"
}

#Player's Name/Intro
name = str(input(f"Hello Brave Adventurer! Please enter your name: "))
print()
players_name = name.capitalize()
print(f"Hello " + players_name + "! Welcome to Dungeon Crawler! Your goal is to escape three dangerous dungeons ahead of you. Be ready to use you brain, as well as your brawn!")
print()

#Dungeon Choosing
def dungeon_choosing():
    global chosen_dungeon , dungeons_left
    while game_playing:
        chosen_dungeon = input(f"Carefully choose a dungeon from the list - (Crypt Dungeon, Desert Dungeon, or Wooded Dungeon): ").capitalize()
        
        if chosen_dungeon == 'Crypt' or chosen_dungeon == 'Desert' or chosen_dungeon == 'Wooded':
            print()
            print(f"Prepare to enter the {chosen_dungeon} Dungeon! ")
            break
        if chosen_dungeon == "Crypt":
            dungeons_left = ["Wooded" , "Desert"]
        elif chosen_dungeon == "Wooded":
            dungeons_left = ["Crypt" , "Desert"]
        elif chosen_dungeon == "Desert":
            dungeons_left = ["Wooded" , "Crypt"]
        else:
            print()
            print(f"That is not an option. Please type the name of the Dungeon. (Exclude the word Dungeon)")
            print()

#Dungeon Encounters
def dungeon_encounter():
    while game_playing:
        global encounter
        encounter = random.choice(["riddle" , "puzzle" , "monster"])
        print()
        if chosen_dungeon == "Crypt":
            if encounter == "riddle": 
                print(crypt["riddle"])
                riddle_answer = input("Be aware but type your answer here: ").lower()
                if riddle_answer == crypt_answer["riddle]"]:
                    print("You got it right!")
                else:
                    print("You got it wrong! Prepare to die!")
                    game_playing = False
                    sys.exit
            elif encounter == "puzzle":
                
        print()
        

dungeon_choosing()
dungeon_encounter()