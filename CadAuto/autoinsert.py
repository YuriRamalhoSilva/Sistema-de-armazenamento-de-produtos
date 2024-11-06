import pyautogui as ag
import shutil
import os
import pyperclip as pc
import csv
from time import sleep


class autoinsert:

    def Auto_Insert(caminho):

        filename = os.path.basename(caminho)
        print(filename)

        destino_relativo = "Sistema-de-armazenamento-de-produtos/CadAuto"
        destino_absoluto = os.path.abspath(destino_relativo)

        if not os.path.exists(destino_absoluto):
            shutil.copy(caminho, destino_absoluto)
            print(f"Arquivo copiado em {destino_absoluto}")
        else:
            print(f"Arquivo já existe em {destino_absoluto}")

        with open(caminho, mode="r", encoding="latin1") as arquivo:
            leitor = csv.reader(arquivo)

            next(leitor, None)

            for row in leitor:
                sleep(0.5)
                nome = row[0]
                pc.copy(nome)
                ag.hotkey("ctrl", "v")
                ag.press("tab")
                sleep(0.5)
                quantidade = int(row[1])
                pc.copy(quantidade)
                ag.hotkey("ctrl", "v")
                ag.press("tab")
                sleep(0.5)
                preco = float(row[2])
                pc.copy(preco)
                ag.hotkey("ctrl", "v")
                sleep(0.5)
                ag.press("enter")
                sleep(0.5)
                ag.press("enter")
                ag.press("tab")
                ag.press("tab")
                ag.press("tab")
                ag.press("tab")
                ag.press("tab")
                ag.press("tab")
                ag.press("tab")
                ag.press("tab")

        pass
