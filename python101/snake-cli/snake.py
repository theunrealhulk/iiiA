import os,time
from enum import Enum

# GAME VARIABLES
gameRunning:bool=False
initialSnakeSize:int=2
speed:float=5.0
interval_secs:float=.461
class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT= 4

directions:Direction = [Direction.RIGHT]

def main():
    decision = startGame()
    global gameRunning
    match(decision.lower()):
        case 'x':
            _showScreen("ui/user-ended-program.txt")
        case 's':
            gameRunning=True
            runGame()

def startGame():
    _showScreen("ui/start.txt")
    user_input = input("Please enter 's' or 'x': ")
    while(user_input.lower()!='s' and user_input.lower()!='x'):
        user_input=input ('invalid input type either "s" or x: ')
    return user_input


def runGame():
    global interval_secs
    print(f"starting game {gameRunning}")
    while(gameRunning):
        time.sleep(interval_secs)
        update()



def endGame():
    _showScreen("ui/end.txt")
    user_input = input("Please enter 's' or 'x': ")
    while(user_input.lower()!='s' and user_input.lower()!='x'):
        user_input=input ('invalid input type either "s" or x: ')

def _showScreen(screenFilePath):
    __clear_console()
    with open(screenFilePath, "r") as file:
        content = file.read()
    print(content)

def __clear_console():
    """Clears the console screen based on the operating system."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        os.system('clear')
i=0
def update():
    global i
    print(f"game runnin {i}")
    i=i+1

main()
