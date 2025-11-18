from enum import Enum
import threading

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Block(Enum):
    EMPTY=1 # ' '
    WALL=1  # '▓'
    FOOD=2  # '*'
    PLAYER=3# 'o' or '-' or '|'

# Global game state
gameRunning: bool = False
interval_secs: float = 0.3
current_direction: Direction = Direction.RIGHT

# Lock for thread-safe access
direction_lock = threading.Lock()