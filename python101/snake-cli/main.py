import time
from ui import showScreen
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
            showScreen("ui/user-ended-program.txt")
        case 's':
            gameRunning=True
            runGame()

def startGame():
    showScreen("ui/start.txt")
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
    showScreen("ui/end.txt")
    user_input = input("Please enter 's' or 'x': ")
    while(user_input.lower()!='s' and user_input.lower()!='x'):
        user_input=input ('invalid input type either "s" or x: ')


i=0
def update():
    print(f"game runnin {i} current snake direction is {directions}")

main()
