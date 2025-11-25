
import time
from ui import showToScreenText
import game_state 
from input_handler import start_input_thread




def main():
    choice = startGame()
    if choice == 'x':
        showToScreenText("ui/user-ended-program.txt")
        return
    game_state.gameRunning = True
    start_input_thread()
    runGame()


def startGame():
    showToScreenText("ui/start.txt")
    user_input = input("Please enter 's' or 'x': ")
    while(user_input.lower()!='s' and user_input.lower()!='x'):
        user_input=input ('invalid input type either "s" or x: ')
    return user_input


def runGame():
    print(f"Game started! {game_state.gameRunning}")   
    while game_state.gameRunning:                      
        time.sleep(game_state.interval_secs)
        update()

def endGame():
    showToScreenText("ui/end.txt")
    sleep(3)
    startGame()
    

def update():
    with game_state.direction_lock:
        dir_now = game_state.current_direction
    game_state.save_board_to_file()
    checkifGameEnded()

def checkifGameEnded():
    if not game_state.gameRunning:
        if game_state.isGomeLost:
            showToScreenText("ui/end.txt")
        elif game_state.isGameEnded:
            showToScreenText("ui/user-ended-program.txt")

if __name__ == "__main__":
    main()
