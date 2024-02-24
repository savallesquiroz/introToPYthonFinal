# INF360 - Programming in Python
# Steve Alexander Valles Quiroz
# Final Project

'''
This program will create a laybrinth for the user to scape with movments for each direction.
The user position in the map is p and its goal is to find its way to E which represents the exit.
User starts with 10 lives and will lose lives when hittin the wall.
'''

#User can chose to either move typing (up/down/left/right) or (w/a/s/d). Once user reaches exit position, the game will end.

#Import functions and map.
try:
    from myFunctions import *
    logging.debug("myFunctions.py loaded succesfully")
except ModuleNotFoundError:
    print("myFunctions.py is missing")
    logging.critical("myFunctinos.py is missing!")
    print("Program will now exit...")
    sys.exit()

# Declare player position.
player_pos = [9, 9]

# Declare exit position.
exit_pos = [9, 0]

#-------------------------------------------------------------------------------------------------------------------------

#GAME
#Print Welcome Function
username = print_welcome(welcome()) #receive username from print_welcome function
#Initialize player with the username
player = Player(username, 0, player_pos, 10)
while player.is_alive():
    print_map(map, player.player_pos)#Print map with player position.
    direction = input("Enter a direction (up/down/left/right) or (w/a/s/d): ")#Receive movement input from user.
    player.move_player(direction)#Display updated map with updated user position.
    if end_game(player.player_pos, exit_pos):  # End the game when user matches exit position.
        print("Congratulations! You reached the exit!")
        print(player.description())
        input()  # Just so user can see end art display
        break
    if not player.is_alive():
        print("Game over! You lost all your lifes.")
        input()
