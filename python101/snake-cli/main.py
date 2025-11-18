
import time
from ui import showScreen
import game_state 
from input_handler import start_input_thread




def main():
    choice = startGame()
    if choice == 'x':
        showScreen("ui/user-ended-program.txt")
        return
    game_state.gameRunning = True
    start_input_thread()
    runGame()


def startGame():
    showScreen("ui/start.txt")
    user_input = input("Please enter 's' or 'x': ")
    while(user_input.lower()!='s' and user_input.lower()!='x'):
        user_input=input ('invalid input type either "s" or x: ')
    return user_input


def runGame():
    print(f"Game started! {game_state.gameRunning}")   # FIXED
    while game_state.gameRunning:                      # FIXED
        time.sleep(game_state.interval_secs)
        update()

def endGame():
    showScreen("ui/end.txt")
    user_input = input("Please enter 's' or 'x': ")
    while(user_input.lower()!='s' and user_input.lower()!='x'):
        user_input=input ('invalid input type either "s" or x: ')


def update():
    with game_state.direction_lock:
        dir_now = game_state.current_direction
    print(f"Game tick... direction = {dir_now.name}")

if __name__ == "__main__":
    main()
