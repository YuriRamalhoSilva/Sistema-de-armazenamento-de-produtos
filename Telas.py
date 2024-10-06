import PySimpleGUI as sg  # Importação da biblioteca de interface e apelidando de sg


def TelaLogin():  # metodo de funcionamento do login e sua interface
    layout = [
        [sg.Text("Faça seu Login!")],
        [sg.Text("LOGIN "), sg.Input(key="Login", size=(30))],
        [sg.Text("SENHA"), sg.Input(key="Senha", password_char="*", size=(30))],
        [sg.Button("Logar"), sg.Button("Sair")],
    ]
    janelalog = sg.Window("LOGAR", layout)

    while True:
        evento, valores = janelalog.read()

        if evento in (sg.WIN_CLOSED, "Sair"):
            janelalog.close()
            return None

        if evento == "Logar":
            user = valores["Login"]
            senha = valores["Senha"]
            # AUTENTICAÇAO DE LOGIN E SENHA#
            if user == "yuri" and senha == "6767":
                janelalog.close()
                return True  # Retorna True para abrir a telaSys


# Função para criar a tela de cadastro de produtos
def TelaSys():  # metodo de funcionamento da Inserção de produtos e sua interface
    layout = [
        [sg.Text("Cadastro de Produtos!")],
        [sg.Input(key="Nome"), sg.Text("Nome")],
        [sg.Input(key="Quant"), sg.Text("Quantidade")],
        [sg.Input(key="Preco"), sg.Text("Preço")],
        [sg.Button("Inserir Produto")],
        [sg.Listbox(values=[], size=(80, 23), key="lista", enable_events=True)],
        [sg.Button("Deslogar")],
        [sg.Button("Auto-Insert")],
    ]
    janelasys = sg.Window("Sistema", layout, size=(600, 620), location=(400, 50))

    # vetor de produtos
    produtos = []

    while True:
        evento, valores = janelasys.read()
        if evento == sg.WIN_CLOSED:
            janelasys.close()
            return None

        if evento == "Inserir Produto":
            produto = (valores["Nome"], valores["Quant"], valores["Preco"])

            if produto:
                produtos.append(produto)

                janelasys["lista"].update(produtos)
                janelasys["Nome"].update("")
                janelasys["Quant"].update("")
                janelasys["Preco"].update("")
        elif evento == "Deslogar":
            janelasys.close()
            return "Deslogar"


# Loop principal
if __name__ == "__main__":
    while True:
        if (
            TelaLogin()
        ):  # Lógica para voltar para a tela de login ao clicar em "Deslogar"
            resposta = (
                TelaSys()
            )  # Atribuindo a ação de deslogar para a variável resposta
            if resposta == "Deslogar":
                continue  # "CONTINUE" para voltar para o começo do while
        break
