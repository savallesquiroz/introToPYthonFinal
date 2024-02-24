#LOGGING TO A FILE
import logging
logging.basicConfig(filename='myProgramLog.txt',
                    level=logging.DEBUG,
                    format='%(asctime)s -  %(levelname)s -  %(message)s')



#ART FUNCTIONS

#Welcome art
def welcome():
    welcome = '''
  ╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗  ╔╦╗╦ ╦  ╦  ╔═╗╔╗ ╦ ╦╦═╗╦╔╗╔╦╗╦ ╦
  ║║║║╣ ║  ║  ║ ║║║║║╣    ║ ║ ║  ║║║╚╦╝  ║  ╠═╣╠╩╗╚╦╝╠╦╝║║║║║ ╠═╣
  ╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝   ╩ ╚═╝  ╩ ╩ ╩   ╩═╝╩ ╩╚═╝ ╩ ╩╚═╩╝╚╝╩ ╩ ╩
--------------------------------------------------------------------
'''
    return welcome

#End Game Art
def end_art():
    end_art = '''

------------------------------------------------------
   ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╔═╗   ╦ ╦╔═╗╦ ╦  ╦ ╦╔═╗╔╗╔┬
   ║  ║ ║║║║║ ╦╠╦╝╠═╣ ║ ╚═╗   ╚╦╝║ ║║ ║  ║║║║ ║║║║│
   ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝┘   ╩ ╚═╝╚═╝  ╚╩╝╚═╝╝╚╝o
------------------------------------------------------
'''
    return end_art
#---------------------------------------------------------------------------------------------------------------------------

#LABYRINTH MAP

map = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],#0
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],#1
    ['#', ' ', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#'],#2
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],#3
    ['#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],#4
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],#5
    ['#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],#6
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],#7
    ['#', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#'],#8
    ['E', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ','#'], #9
    ['#','#','#','#','#','#','#','#','#','#','#']           #10
]

#-----------------------------------------------------------------------------------------------------------------------------

#Declare Player Class.
class Player():
    
    def __init__(self, username, score, player_pos, lives):
        self.username = username
        self.score = score
        self.player_pos = player_pos
        self.lives = 10
        
    #Methods
    #Username method
    def description(self):
        score = self.user_score()
        return f"{self.username} finished the game with {self.lives} lives and a score of {score}"
        logging.info(f"{self.username} finished the game with {self.lives} lives and a total score of {score} out of 100!")#log info to file
    #Function to move the player
    def move_player(self, direction): #Receive direction from user input and player position from program.
        if direction == 'up' or direction == 'w':
            if map[self.player_pos[0]-1][self.player_pos[1]] != '#': #Only moves the first index up, which represents 'y' position. 'x' remains the same.
                self.player_pos[0] -= 1
            #Lower life when user hits the wall.
            elif map[self.player_pos[0]-1][self.player_pos[1]] == '#':
                print("You hit a wall! You lose a life.")
                logging.debug("Movement error, user hit the wall")#log invalid movement debug to file
                self.lives -= 1
        elif direction == 'down' or direction == 's':
            if map[self.player_pos[0]+1][self.player_pos[1]] != '#': #Only moves the first index down, which represents 'y' position. 'x' remains the same.
                self.player_pos[0] += 1
            #Lower life when user hits the wall.
            elif map[self.player_pos[0]+1][self.player_pos[1]] == '#':
                print("You hit a wall! You lose a life.")
                logging.debug("Movement error, user hit the wall")#log invalid movement debug to file
                self.lives -= 1
        elif direction == 'left' or direction == 'a':
            if map[self.player_pos[0]][self.player_pos[1]-1] != '#': #Only moves the second index left, which represents 'x' position. 'y' remains the same.
                self.player_pos[1] -= 1
            #Lower life when user hits the wall.
            elif map[self.player_pos[0]][self.player_pos[1]-1] == '#':
                print("You hit a wall! You lose a life.")
                logging.debug("Movement error, user hit the wall")#log invalid movement debug to file
                self.lives -= 1
        elif direction == 'right' or direction == 'd':
            if map[self.player_pos[0]][self.player_pos[1]+1] != '#': #Only moves the second index right, which represents 'x' position. 'y' remains the same.
                self.player_pos[1] += 1
            #Lower life when user hits the wall.
            elif map[self.player_pos[0]][self.player_pos[1]+1] == '#':
                print("You hit a wall! You lose a life.")
                logging.debug("Movement error, user hit the wall")#log invalid movement debug to file
                self.lives -= 1
        elif direction != 'right' or direction != 'left' or direction != 'up' or direction != 'down' or direction != 'a' or direction !='s' or direction !='d' or direction != 'w':
            print(wrong_input()) #When user does not introduce a correct input, display error message.
        elif self.player_pos == exit_pos:
            exit
    
    #Finish program when user loses all its lifes
    def is_alive(self):
        return self.lives > 0
    #Print user_score based on lives remaining
    def user_score(self):
        if self.lives > 8:
            return 'EXCELLENT'
        elif self.lives > 6:
            return 'Good'
        elif self.lives > 4:
            return 'bad'
        else:
            return 'AWFUL'

#-------------------------------------------------------------------------------------------------------------------------------

#PROGRAM FUNCTIONS

#Wrong input
def wrong_input():
    wrong_input = "\n\nI'm sorry, you introduced a wrong value. Remember to type(up/down/left/right) or (w/a/s/d).\n\n"

    return wrong_input

#Welcome user function
def print_welcome(welcome):
    print(welcome)
    #Prompt user for instructions
    print("Your position in the map is 'p' and your goal is to survive your way to the exit('E').")
    print("You start with 10 lives and will lose 1 each time you hit the wall.")
    print("In order for you to move, you need to type (up/down/left/right) as you desire.")
    print("You can also use typical videogame positional movements(w/a/s/d) to move faster.\n\n")
    #Ask user to enter username
    username = input("Please, choose an username(only lowercase and numbers): ")
    logging.info(f"Username is: {username}")#log info to file

    logging.debug("Checking name for validity...")
    while len(username) > 16 or username != username.lower() or username == "":#Ask for username until input is valid
        username = input("Please, choose an username(only lowercase and numbers): ")
        logging.info(f"Username is: {username}")#log username info to file

    logging.debug("Checking name for validity...")#log username validity debug to file
    if len(username) > 16:
        print("Username must be less than 16 characters.")
        logging.debug("Error, user introduced a username longer than 16 characters.")#log invalid lenght debug to file
    elif username != username.lower():
        print("Username must not contain uppercase letters.")
        logging.debug("Error, user introduced uppercase letters")#log invalid uppercase debug to file
    elif username == "":
        print("Username must not be empty.")
        logging.debug("Error, user introduced an empty username")#log invalid empty username debug to file
    else:
        print("Username is valid!")
        print("\nPlease, press any key to continue")
        logging.debug("Username is valid!")#log valid username debug to file
        return username
    input()
    
    print("*" * 20)
    print('GAME STARTS NOW'.center(20))
    print("*" * 20)
    print("\n")


# Function to print labyrinth with player position
def print_map(map, player_pos):
    for i, row in enumerate(map): #Use enumerate to return both, map and player position in the loop
        for j, cell in enumerate(row):#iterate through each row and column in the map
            if [i, j] == player_pos:#Display 'p' when player position is matched
                print('P', end='')
            else:                   #Otherwise, display empty cell.
                print(cell, end='')
        print()


# Function to end game
def end_game(player_pos, exit_pos):
    if player_pos == exit_pos: #When player position matches exit position, end the game and display end art.
        print(end_art())
        return True
    return False
