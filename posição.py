import pyautogui
from time import sleep
sleep(2)
try:
    while True:
        # Pega a posição atual do mouse
        x, y = pyautogui.position()
        
        # Mostra a posição do mouse
        print(f"Mouse position: ({x}, {y})", end="\r")
        
        # Espera um pouco para não sobrecarregar o terminal
        sleep(0.1)

except KeyboardInterrupt:
    print("\nPrograma encerrado.")
