import sys
import threading
import time
import os
from datetime import datetime

print_lock = threading.Lock()




def getch():
    if sys.platform.startswith("win"):
        import msvcrt
        return msvcrt.getch().decode(errors="ignore")
    else:
        import tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch


def key_listener(state):
    print("[KEY LISTENER] Started. Press 'x' to exit.")

    while not state["stop"]:
        ch = getch()

        if sys.platform.startswith("win"):
            import msvcrt
            if ch in ('\x00', '\xe0'):
                ch2 = msvcrt.getch().decode(errors="ignore")
                state["last_key"] = f"ARROW {repr(ch2)}"
                continue
            if ch == 'x':
                state["last_key"] = 'x'
                state["stop"] = True
                break
            state["last_key"] = ch
            continue

        # Linux/Mac
        if ch == '\x1b':
            import select
            if select.select([sys.stdin], [], [], 0.01)[0]:
                ch2 = getch()
                if ch2 == '[':
                    ch3 = getch()
                    state["last_key"] = f"ARROW {repr(ch3)}"
                    continue

        if ch == 'x':
            state["last_key"] = 'x'
            state["stop"] = True
            break

        state["last_key"] = ch


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    FPS = 42  # Target frames per second
    frame_duration = 1.0 / FPS  # seconds per loop

    state = {"stop": False, "last_key": "None"}

    t = threading.Thread(target=key_listener, args=(state,), daemon=True)
    t.start()

    while not state["stop"]:
        start_time = time.time()  # loop start

        with print_lock:
            clear_console()
            print("=== Program Running ===")
            print("Current time:", datetime.now().strftime("%H:%M:%S"))
            print("Last pressed key:", state["last_key"])
            print("Press 'x' to exit.")

        # calculate time spent in this iteration
        elapsed = time.time() - start_time
        sleep_time = max(0, frame_duration - elapsed)
        time.sleep(sleep_time)

    print("[PROGRAM] Ended.")


if __name__ == "__main__":
    main()
