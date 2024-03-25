from pynput import mouse
import json
import threading
import time

# Lista para armazenar as ações do mouse
mouse_actions = []

# Variável de controle para encerrar a execução da thread
exit_thread = threading.Event()

def on_click(x, y, button, pressed):
    # Adiciona ação do mouse à lista
    action = {"x": x, "y": y, "button": str(button), "pressed": pressed}
    mouse_actions.append(action)

def mouse_listener_thread():
    # Cria um listener para o mouse
    with mouse.Listener(on_click=on_click) as listener:
        # Aguarda até que a variável de controle seja definida
        exit_thread.wait()

# Inicia uma thread para o listener do mouse
listener_thread = threading.Thread(target=mouse_listener_thread)
listener_thread.start()

try:
    # Mantém o programa rodando por 10 segundos (ou qualquer outro valor desejado)
    time.sleep(10)
finally:
    # Define a variável de controle para encerrar a execução da thread
    exit_thread.set()

    # Aguarda até que a thread seja encerrada
    listener_thread.join()

    # Salva as ações do mouse em um arquivo JSON
    with open('mouse_actions.json', 'w') as file:
        json.dump(mouse_actions, file)
