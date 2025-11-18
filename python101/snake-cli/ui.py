import os
import sys

def showScreen(screenFilePath):
    clear_console()
    with open(screenFilePath, "r") as file:
        content = file.read()
    print(content)

def clear_console():
    """Clears the console screen using ANSI escape codes for speed."""
    # Move cursor to home position (top-left)
    #sys.stdout.write('\033[H')
    # Clear the screen from the cursor down
    #sys.stdout.write('\033[J')
    # Ensure the changes are rendered immediately
    #sys.stdout.flush()

    # Optional: Keep the os.system fallback if ANSI codes don't work on a very specific terminal setup
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')