import random
#Varaibles
game_playing = True
all_riddles = {"riddle1" : "Riddle: I am alive but I am not human. I was not born but I was made. My body was created from wood. My best friend is a cricket. What am I? " , 
               "riddle2" : 2 , 
               "riddle3" : 3 , 
               "riddle4" : 4 , 
               "riddle5" : 5
               }
all_riddle_answers = {"riddle1" : "pinocchio",
                      "riddle2" : 2,
                      "riddle3" : 3,
                      "riddle4" : 4,
                      "riddle5" : 5
                      }
all_monsters = {"Zobmie" : "You have encountered a Zombie! What should you do?",
                "Skeleton" : 2,
                "Vampire" : 3,
                "Troll" : 4,
                "Ghost" : 5
                }
all_monsters_answers = {"Zobmie" : 1,
                        "Skeleton" : 2,
                        "Vampire" : 3,
                        "Troll" : 4,
                        "Ghost" : 5}
all_puzzles = {}
all_possible_encounters = [all_riddles , 
                           all_monsters ,
                           all_puzzles ,]

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

#Dungeon Encounters
def dungeon_prompts():
   global riddle
   global answer
   riddle = random.choice(all_possible_encounters)
   answer = all_possible_encounters.keys()
   print(answer)
   


dungeon_choosing()
dungeon_prompts()