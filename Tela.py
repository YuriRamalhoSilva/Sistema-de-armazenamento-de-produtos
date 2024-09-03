import PySimpleGUI as sg
from Telasys import janelasys


# Criação da tela de login
layoutlog = [
    [sg.Text("Faça seu Login!")],
    [sg.Text("LOGIN "), sg.Input(key="Login", size=(30))],
    [sg.Text("SENHA"), sg.Input(key="Senha", password_char="*", size=(30))],
    [sg.Button("Logar"), sg.Button("Sair")],
]
janela1 = sg.Window("TelaLogin", layoutlog)

# Lista de produtos
produtos = []

# Loop de eventos do Login
while True:
    evento1, valores1 = janela1.read()

    # Se o usuário fechar a janela ou clicar em 'Sair'
    if evento1 == sg.WINDOW_CLOSED or evento1 == "Sair":
        break

    # Se o usuário clicar em 'Logar'
    if evento1 == "Logar":
        janela2 = janelasys()
        janela1["Login"].update("")
        janela1["Senha"].update("")
        janela1.hide()

        # Loop da Tela sys
        while True:
            evento2, valores2 = janela2.read()
            if evento2 == "Inserir Produto":
                produto = (valores2["Nome"], valores2["Quant"], valores2["Preco"])

                if produto:
                    produtos.append(produto)

                    janela2["lista"].update(produtos)
                    janela2["Nome"].update("")
                    janela2["Quant"].update("")
                    janela2["Preco"].update("")

            # Se o usuário fechar a janela ou clicar em 'Fechar'
            if evento2 == sg.WINDOW_CLOSED:
                janela1.close()
                janela2.close()
                break
            if evento2 == "Deslogar":
                janela2.close()
                janela1.un_hide()
                break
janela1.close()
