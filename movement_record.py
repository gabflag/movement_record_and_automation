import time
import pyautogui
from pynput.mouse import Listener

def on_move(x, y):
    with open('mouse_log.txt', 'a') as file:
        file.write(f"Mouse movement: ({x}, {y})\n")

def on_click(x, y, button, pressed):
    action = "Pressed" if pressed else "Released"
    with open('mouse_log.txt', 'a') as file:
        file.write(f"{action} - Button {button} at ({x}, {y})\n")

def on_scroll(x, y, dx, dy):
    with open('mouse_log.txt', 'a') as file:
        file.write(f"Mouse scroll at ({x}, {y}): ({dx}, {dy})\n")

def automatic_movement():
    with open('mouse_log.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split(' - ')
        if "Mouse movement" in parts[0]:
            coords = parts[0].split(":")[1].strip()[1:-1].split(',')
            x, y = int(coords[0]), int(coords[1])
            pyautogui.moveTo(x, y)
        elif "Pressed" in parts[0]:
            coords = parts[1].split(" at ")[1].strip()[1:-1].split(',')
            x, y = int(coords[0]), int(coords[1])
            pyautogui.click(x, y)

        elif "Mouse scroll" in parts[0]:
            values = parts[1].strip()[1:-1].split(':')
            dx, dy = int(values[0]), int(values[1])
            pyautogui.scroll(dx, dy)
        else:
            print('Error')

        time.sleep(0.1)

def record_movement():
    # Record mouse movement
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()

# record_movement()
# automatic_movement()
