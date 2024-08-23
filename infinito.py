import pyautogui
from time import sleep


while True:

        # Espera inicial de 5 segundos para dar tempo de trocar de janela ou preparar o ambiente
        sleep(4.2)

        # Pressiona Ctrl + A (selecionar tudo)
        pyautogui.hotkey('ctrl', 'a')
        sleep(0.5)

        # Pressiona Ctrl + C (copiar)
        pyautogui.hotkey('ctrl', 'c')
        sleep(0.5)

        # Pressiona Alt + Tab (muda de janela)
        pyautogui.hotkey('alt', 'tab')
        sleep(0.5)

        # Pressiona Ctrl + V (colar)
        pyautogui.hotkey('ctrl', 'v')
        sleep(0.5)

        # Pressiona Alt + Tab novamente (volta para a janela anterior)
        pyautogui.hotkey('alt', 'tab')
        sleep(0.5)

        # Segura a tecla End por 2 segundos (vai para o final da página ou documento)
        pyautogui.keyDown('end')
        sleep(2)
        pyautogui.keyUp('end')

        # Clica com o botão esquerdo do mouse na posição (694, 858)
        pyautogui.leftClick(694, 858)

