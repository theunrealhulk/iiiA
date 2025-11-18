
import os
import platform

def clear_console():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def empty_file(filename="screen.txt"):
    open(filename, "w", encoding="utf-8").close()