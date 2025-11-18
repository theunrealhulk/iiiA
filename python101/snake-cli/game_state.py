from enum import Enum
import threading

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

# Global game state
gameRunning: bool = False
interval_secs: float = 0.3
current_direction: Direction = Direction.RIGHT

# Lock for thread-safe access
direction_lock = threading.Lock()