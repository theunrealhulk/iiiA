import sys, threading
import game_state 

def getch():
    """
    Read a single keypress from the user without requiring Enter.
    Works on Windows, Linux, and macOS.
    Returns the character as a string (e.g., 'w', '\x1b' for Escape, etc.).
    """
    if sys.platform.startswith('win'):
        # Windows
        import msvcrt
        key = msvcrt.getch()
        # msvcrt.getch() returns bytes; decode special keys properly
        if key in (b'\xe0', b'\x00'):  # Special keys (arrows, etc.)
            key = msvcrt.getch()       # Get the actual key code
        return key.decode('utf-8', errors='ignore')
    
    else:
        # Linux and macOS
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def input_listener():
    """Listens for user input without blocking."""
    while game_state.gameRunning:
        ch = getch()
        with game_state.direction_lock:
            if ch in ['w', 'W']:
                game_state.current_direction = game_state.Direction.UP
            elif ch in ['s', 'S']:
                game_state.current_direction = game_state.Direction.DOWN
            elif ch in ['a', 'A']:
                game_state.current_direction = game_state.Direction.LEFT
            elif ch in ['d', 'D']:
                game_state.current_direction = game_state.Direction.RIGHT
            elif ch.lower() == 'x': #to exit hgame while it's running 
                game_state.gameRunning = False

def start_input_thread():
    """Starts input listener in a background thread."""
    t = threading.Thread(target=input_listener, daemon=True)
    t.start()