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

        shutil.copy(caminho, destino_absoluto)
        print(f"Arquivo copiado em {destino_absoluto}")

        with open(caminho,mode='r',encoding='latin1') as arquivo:
            leitor = csv.reader(arquivo)

            next(leitor, None)

            for row in leitor:
                ag.click(249,148,duration=1)
                nome = row[0]
                pc.copy(nome)
                ag.hotkey('ctrl','v')
                ag.click(330,174,duration=1)
                quantidade = int(row[1])
                pc.copy(quantidade)
                ag.hotkey('ctrl','v')
                ag.click(322,200,duration=1)
                preco = float(row[2])
                pc.copy(preco)
                sleep(1)
                ag.hotkey('ctrl','v')
                ag.press('enter')

                


    
        
        pass