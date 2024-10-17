import PySimpleGUI as sg  # Importação da biblioteca de interface e apelidando de sg
import Sistema

# TELA LOGAR vvvvv


def TelaLogin():

    layout = [
        [sg.Text("Faça seu Login!")],
        [sg.Text("LOGIN "), sg.Input(key="Email", size=(30))],
        [sg.Text("SENHA"), sg.Input(key="Senha", password_char="*", size=(30))],
        [sg.Button("Logar"), sg.Button("Sair")],
        [sg.Text("Ainda não está cadastrado?")],
        [sg.Button("Cadastre-se")],
    ]
    janelalog = sg.Window("LOGAR", layout)

    while True:
        evento, valores = janelalog.read()

        if evento in (sg.WIN_CLOSED, "Sair"):
            janelalog.close()
            return None

        if evento == "Logar":
            user = valores["Email"]
            senha = valores["Senha"]
            # AUTENTICAÇAO DE LOGIN E SENHA#
            if user == "yuri" and senha == "6767":
                janelalog.close()
                return "Logar"  # Retorna True para abrir a telaSys

        if evento == "Cadastre-se":
            janelalog.close()
            return "Cadastre-se"


# TELA CADASTRO USUARIO vvvvv


def TelaCadUser():
    layout = [
        [sg.Text("Coloque seu email e senha!")],
        [sg.Text("Email ")],
        [sg.Input(key="Email")],
        [sg.Text("Senha ")],
        [sg.Input(key="Senha", password_char="*")],
        [sg.Text("Confirme sua senha")],
        [sg.Input(key="confsenha", password_char="*")],
        [sg.Button("Cadastrar")],
        [sg.Button("Voltar")],
    ]
    janelaCadUser = sg.Window("CADASTRO USUARIO", layout)

    while True:
        evento, valores = janelaCadUser.read()

        if evento in (sg.WIN_CLOSED, "Voltar"):
            janelaCadUser.close()
            return "Voltar"

        if evento == "Cadastrar":
            email = valores["Email"]
            senha = valores["Senha"]
            confsenha = valores["confsenha"]
            if senha != confsenha:
                sg.popup("Erro", "A confirmação da senha não foi validada!")
            else:
                retorno, erro = Sistema.Sistema.Cad_User(email, senha)

                if retorno == "sememailousenha":
                    sg.popup("Erro", "Erro ao Cadastrar, digite seu usuário e senha!")
                elif retorno == "emailinvalido":
                    sg.popup("Erro", "O email digitado não é válido!")
                elif retorno == "errobanco":
                    sg.popup("Erro", erro)
                else:
                    sg.popup("Cadastro Concluído!", "Usuário cadastrado com sucesso!")


# TELA CADASTRO PRODUTO vvvvv


def TelaSys():  # Método de funcionamento da Inserção de produtos e sua interface
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
        resp1 = TelaLogin()
        if resp1 == "Cadastre-se":
            resp2 = TelaCadUser()
            if resp2 == "Voltar":
                continue

        if resp1 == "Logar":
            # Lógica para voltar para a tela de login ao clicar em "Deslogar"
            resp3 = TelaSys()  # Atribuindo a ação de deslogar para a variável resposta
            if resp3 == "Deslogar":
                continue  # "CONTINUE" para voltar para o começo do while

        break
