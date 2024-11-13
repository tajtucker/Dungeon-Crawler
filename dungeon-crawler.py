import random
#Varaibles
game_playing = True
crypt = {"riddle":"I slip through the murk, silent and quick, With scales and teeth, sharp and slick. What am I?" , 
"puzzle" : "In a swamp, there are 3 frogs on a lily pad. Each frog catches 2 flies. How many flies are caught in total?" ,
"monster" : "You encounter a Slime! Would you like to run or fight?"
}

desert = {"riddle":}

#Player's Name/Intro
name = str(input(f"Hello Brave Adventurer! Please enter your name: "))
print()
players_name = name.capitalize()
print(f"Hello " + players_name + "! Welcome to Dungeon Crawler! Your goal is to escape three dangerous dungeons ahead of you. Be ready to use you brain, as well as your brawn!")
print()

#Dungeon Choosing
def dungeon_choosing():
    global chosen_dungeon
    while game_playing:
        chosen_dungeon = input(f"Carefully choose a dungeon from the list - (Crypt Dungeon, Desert Dungeon, or Wooded Dungeon): ").capitalize()
        
        if chosen_dungeon == 'Crypt' or chosen_dungeon == 'Desert' or chosen_dungeon == 'Wooded':
            print()
            print(f"Prepare to enter the {chosen_dungeon} Dungeon! ")
            break 
        else:
            print()
            print(f"That is not an option. Please type the name of the Dungeon. (Exclude the word Dungeon)")
            print()


   

dungeon_choosing()
