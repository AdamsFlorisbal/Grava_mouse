from pynput.mouse import Controller, Button
import json
import time

def reproduzir_acoes_do_mouse(actions):
    mouse = Controller()

    for action in actions:
        x, y = action["x"], action["y"]
        button = action["button"]
        pressed = action["pressed"]

        mouse.position = (x, y)

        if button == "Button.left":
            if pressed:
                mouse.press(Button.left)
            else:
                mouse.release(Button.left)
        elif button == "Button.right":
            if pressed:
                mouse.press(Button.right)
            else:
                mouse.release(Button.right)

        time.sleep(0.1)

if __name__ == "__main__":
    # Carrega as ações do mouse do arquivo JSON
    with open('mouse_actions.json', 'r') as file:
        mouse_actions = json.load(file)

    # Reproduz as ações do mouse
    reproduzir_acoes_do_mouse(mouse_actions)
