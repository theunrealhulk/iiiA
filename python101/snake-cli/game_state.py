from enum import Enum
from utils import clear_console, empty_file
import threading # Assuming this is used elsewhere as indicated by your lock

class Block(Enum):
    EMPTY=1 # ' '
    WALL=2  # '▓'
    FOOD=3  # '*'
    PHEAD=4 # '▶' or '◀' or '▲' OR '▼'
    PTAIL=5 # '-' or '|'

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

# Global game state
gameRunning: bool = False
interval_secs: float = 0.3
current_direction: Direction = Direction.RIGHT
isGomeLost:bool = False
isGameEnded:bool = False

# Lock for thread-safe access
direction_lock = threading.Lock()

# Constants for board size
BOARD_WIDTH = 50
BOARD_HEIGHT = 21
BOARD_SIZE = BOARD_WIDTH * BOARD_HEIGHT

# Initialize board as a list of lists (2D array)
# Fill every spot with Block.EMPTY first
board = [[Block.EMPTY for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# --- Initialize Walls using 2D coordinates [row][col] ---

# Top and Bottom Walls
for col in range(BOARD_WIDTH):
    board[0][col] = Block.WALL          # Top row (index 0)
    board[BOARD_HEIGHT - 1][col] = Block.WALL # Bottom row (index 20)

# Left and Right Walls
for row in range(1, BOARD_HEIGHT - 1):
    board[row][0] = Block.WALL          # Left edge (column 0)
    board[row][BOARD_WIDTH - 1] = Block.WALL # Right edge (column 49)

# Initial snake position (e.g., Row 10, Columns 3, 4, 5)
board[10][3] = Block.PTAIL
board[10][4] = Block.PTAIL
board[10][5] = Block.PHEAD


def drawBoard():
    clear_console()
    # Build entire board as ONE string
    board_str = ""
    for row in range(BOARD_HEIGHT):
        row_str = ""
        for col in range(BOARD_WIDTH):
            block_type = board[row][col]
            match(block_type):
                case Block.EMPTY: char = ' '
                case Block.WALL: char = '▓'
                case Block.FOOD: char = '*'
                case Block.PHEAD:
                    match current_direction:
                        case Direction.UP: char = '▲'
                        case Direction.DOWN: char = '▼'
                        case Direction.LEFT: char = '◀'
                        case Direction.RIGHT: char = '▶'
                case Block.PTAIL:
                    char = '|' if current_direction in [Direction.UP, Direction.DOWN] else '-'
                case _: char = ' '  # Fallback
        
            row_str += char    
        print(row_str)
    print()
        
def empty_file(filename):
    try:
        with open(filename, 'w') as f:
            pass  # File is now empty
        #print(f"{filename} has been emptied.")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except PermissionError:
        print(f"No permission to modify {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def save_board_to_file(filename="screen.txt"):
    empty_file(filename)
    """
    Saves the current game board as text to a file.
    Appends a timestamp + blank line between frames for animation replay.
    """
    from datetime import datetime
    # Put this ONCE when your game starts (before the loop)
    with open(filename, "a", encoding="utf-8") as f:  # 'a' = append
        # Optional: add timestamp/frame separator
        f.write(f"\n--- Frame at {datetime.now().strftime('%H:%M:%S.%f')[:-3]} ---\n")
        
        for row in range(BOARD_HEIGHT):
            row_str = ""
            for col in range(BOARD_WIDTH):
                block_type = board[row][col]
                match block_type:
                    case Block.EMPTY:
                        char = ' '
                    case Block.WALL:
                        char = '▓'
                    case Block.FOOD:
                        char = '*'
                    case Block.PHEAD:
                        match current_direction:
                            case Direction.UP: char = '▲'
                            case Direction.DOWN: char = '▼'
                            case Direction.LEFT: char = '◀'
                            case Direction.RIGHT: char = '▶'
                            case _: char = '?'
                    case Block.PTAIL:
                        char = '|' if current_direction in [Direction.UP, Direction.DOWN] else '-'
                    case _:
                        char = '?'
                row_str += char
            f.write(row_str + "\n")
        
        f.write("\n")  # Extra newline for separation between frames