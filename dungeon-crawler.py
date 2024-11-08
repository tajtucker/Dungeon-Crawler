#Varaibles
dungeon_crpyt = 'crypt'
dungeon_egypt = 'egypt'
dungeon_woods = 'wooded'
game_playing = True

#Beginning Function
def beginning():
    while game_playing:
        name = str(input("Hello Brave Adventurer! Please enter your name: "))
        players_name = name.capitalize()
        print("\fHello " + players_name + "! Welcome to Dungeon Crawler! Your goal is to escape three dangerous dungeons ahead of you. Be ready to use you brain, as well as your brawn!")
        print()
    
        dungeon = input("\fCarefully type the dungeon's name that you wish to enter: Crypt, Egypt, or Wooded: ").lower()
    
        if dungeon != dungeon_crpyt or dungeon_egypt or dungeon_woods:
            print("Please enter a dungeon from the list.")
        elif dungeon == ('crypt'):
            print("\fYou have chosen the Crypt Dungeon! Strap in as you enter your impending doom!")
        elif dungeon == ('egypt'):
            print("\fYou have chosen the Egypt Dungeon! Strap in as you enter your impending doom!")
        elif dungeon == ('wooded'):
            print("\fYou have chosen the Wooded Dungeon! Strap in as you enter your impending doom!")
        

    
    chosen_dungeon = dungeon.capitalize()
    print("\fYou have chosen the " + chosen_dungeon + " Dungeon! Strap in as you enter your impending doom!")

#Main
def main():
    while game_playing == True:
        break


beginning()