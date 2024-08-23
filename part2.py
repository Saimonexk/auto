import pyautogui
from time import sleep

# Lista de palavras a serem usadas
palavras = ["clinica", "imobiliaria", "Loja de roupa feminina", "Loja de Materiais", "Loja de construção", "ótica"]

# Loop para cada palavra da lista
for palavra in palavras:
    
    # Copia a palavra atual para a área de transferência
    pyautogui.hotkey('ctrl', 'c')  # Simula o Ctrl + C para copiar a palavra
    pyautogui.write(palavra)  # Cola a palavra

    # Repete o processo 12 vezes
    for _ in range(12):
        
        # Espera inicial de 5 segundos para dar tempo de trocar de janela ou preparar o ambiente
        sleep(5)

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

        # Clica na posição (694, 858)
        pyautogui.leftClick(694, 858)

        # Clique na posição (304, clinicaclinica169)
        pyautogui.leftClick(304, 169)
        sleep(0.5)

        # Pressiona Shift + Home para selecionar o conteúdo da linha
        pyautogui.hotkey('shift', 'home')
        sleep(0.5)

        # Colar a palavra (Ctrl + V)
        pyautogui.hotkey('ctrl', 'v')
        sleep(0.5)

print("Processo concluído para todas as palavras.")
