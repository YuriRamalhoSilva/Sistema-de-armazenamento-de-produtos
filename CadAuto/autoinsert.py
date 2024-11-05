import pyautogui as ag
import shutil
import os
import csv

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
                nome = row[0]
                quantidade = int(row[1])
                preco = float(row[2])

                print(nome,quantidade,preco)


    
        
        pass