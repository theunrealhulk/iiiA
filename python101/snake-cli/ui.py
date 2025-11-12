import os

def showScreen(screenFilePath):
    clear_console()
    with open(screenFilePath, "r") as file:
        content = file.read()
    print(content)

def clear_console():
    """Clears the console screen based on the operating system."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Unix-like systems (Linux, macOS)
        os.system('clear')