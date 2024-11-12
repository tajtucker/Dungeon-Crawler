#Varaibles
game_playing = True

#Player's Name/Intro
name = str(input(f"Hello Brave Adventurer! Please enter your name: "))
print()
players_name = name.capitalize()
print(f"Hello " + players_name + "! Welcome to Dungeon Crawler! Your goal is to escape three dangerous dungeons ahead of you. Be ready to use you brain, as well as your brawn!")
print()

#Dungeon Choosing
def Dungeon_Choosing():
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
    
        

Dungeon_Choosing()