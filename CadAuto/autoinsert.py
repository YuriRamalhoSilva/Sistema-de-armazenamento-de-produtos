import pyautogui as ag
import shutil


class autoinsert:

    def copy_file_to_CadAuto(caminho):
        origem = caminho
        destino = "C:/Users/yurir/Desktop/CrudPYGit/Sistema-de-armazenamento-de-produtos/CadAuto"

        shutil.copy(origem, destino)
        print(f"Arquivo copiado em {destino}")
