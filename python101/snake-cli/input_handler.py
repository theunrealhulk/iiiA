import sys, threading
import game_state 

def getch():
    """
    Returns a single key press.
    - Normal keys: 'a', 'x', etc.
    - Arrow keys: 'UP', 'DOWN', 'LEFT', 'RIGHT'
    """
    if sys.platform.startswith("win"):
        return getch_windows()

    # Linux/macOS
    import tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    
    try:
        tty.setraw(fd)
        ch1 = sys.stdin.read(1)

        if ch1 == '\x1b':  # ESC
            ch2 = sys.stdin.read(1)
            if ch2 == '[':
                ch3 = sys.stdin.read(1)
                arrows = {
                    'A': 'UP',
                    'B': 'DOWN',
                    'C': 'RIGHT',
                    'D': 'LEFT'
                }
                return arrows.get(ch3, None)
        return ch1

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def getch_windows():
    import msvcrt
    ch = msvcrt.getch()

    # Arrow keys come as:  b'\xe0' THEN another byte
    if ch in [b'\x00', b'\xe0']:
        ch2 = msvcrt.getch()
        arrows = {
            b'H': 'UP',
            b'P': 'DOWN',
            b'M': 'RIGHT',
            b'K': 'LEFT',
        }
        return arrows.get(ch2, None)

    return ch.decode("utf-8", errors="ignore")

def input_listener():
    while game_state.gameRunning:
        key = getch()

        with game_state.direction_lock:

            if key == 'UP' and game_state.current_direction != game_state.Direction.DOWN:
                game_state.current_direction = game_state.Direction.UP

            elif key == 'DOWN' and game_state.current_direction != game_state.Direction.UP:
                game_state.current_direction = game_state.Direction.DOWN

            elif key == 'LEFT' and game_state.current_direction != game_state.Direction.RIGHT:
                game_state.current_direction = game_state.Direction.LEFT

            elif key == 'RIGHT' and game_state.current_direction != game_state.Direction.LEFT:
                game_state.current_direction = game_state.Direction.RIGHT

            elif key == 'x':
                game_state.gameRunning = False
                game_state.isGameEnded=True


def start_input_thread():
    """Starts input listener in a background thread."""
    t = threading.Thread(target=input_listener, daemon=True)
    t.start()