from pynput import mouse
from pynput.mouse import Controller

def on_move(x, y):
    move = 'Pointer moved to {0}'.format((x, y))
    with open('mouse_log.txt', 'a') as file:
        file.write(f"{move}\n")

def on_click(x, y, button, pressed):
    action = 'Pressed' if pressed else 'Released'
    click_info = '{0} at {1}'.format(action, (x, y))

    with open('mouse_log.txt', 'a') as file:
        file.write(f"{click_info}\n")

def on_scroll(x, y, dx, dy):
    scroll_info = 'Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y))
    with open('mouse_log.txt', 'a') as file:
        file.write(f"{scroll_info}\n")

def replay_mouse_events_from_file(filename):
    mouse_controller = Controller()
    
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if 'Pointer moved to' in line:
            _, coords = line.split('to ')
            x, y = map(int, coords.strip('()').split(', '))
            mouse_controller.position = (x, y)

        elif 'Pressed' in line or 'Released' in line:
            if 'Pressed' in line:
                mouse_controller.press(mouse.Button.left)
            else:
                mouse_controller.release(mouse.Button.left)

        elif 'Scrolled' in line:
            if 'down' in line:
                mouse_controller.scroll(0, -1)
            else:
                mouse_controller.scroll(0, 1)


def gravar():
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()

replay_mouse_events_from_file('mouse_log.txt')
