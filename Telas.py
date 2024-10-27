import PySimpleGUI as sg  # Importação da biblioteca de interface e apelidando de sg
import Sistema

# TELA LOGAR vvvvv


def TelaLogin():

    layout = [
        [sg.Text("Faça seu Login!")],
        [
            sg.Column(
                [[sg.Text("LOGIN "), sg.Input(key="Email", size=(30))]], pad=(20, 0)
            )
        ],
        [
            sg.Column(
                [
                    [
                        sg.Text("SENHA"),
                        sg.Input(key="Senha", password_char="*", size=(30)),
                    ]
                ],
                pad=(18, 0),
            )
        ],
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
            retorno = Sistema.Sistema.Aut_Log(user, senha)
            if retorno == "liberado":

                janelalog.close()
                return "Logar"
            elif retorno == "negado":
                sg.popup("Acesso Negado!", "A senha está incorreta!")
            elif retorno == "emailinex":
                sg.popup(
                    "Erro!",
                    "Não foi possivel encontrar um usuário com esse email cadastrado no sistema!",
                )
            elif retorno == "emailinv":
                sg.popup(
                    "Erro!",
                    "Digite um email válido!\nExemplo: emailexemplo@exemplo.com",
                )

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
                retorno = Sistema.Sistema.Cad_User(email, senha)

                if retorno == "sememailousenha":
                    sg.popup("Erro", "Erro ao Cadastrar, digite seu usuário e senha!")
                elif retorno == "emailinvalido":
                    sg.popup("Erro", "O email digitado não é válido!")
                elif retorno == "emailjaexiste":
                    sg.popup("Erro", "Email já cadastrado!")
                else:
                    sg.popup("Cadastro Concluído!", "Usuário cadastrado com sucesso!")


# TELA CADASTRO PRODUTO vvvvv


def TelaSys():  # Método de funcionamento da Inserção de produtos e sua interface

    layout = [
        [sg.Text("Cadastro de Produtos!")],
        [sg.Column([[sg.Text("Nome"), sg.Input(key="Nome")]], pad=(55, 0))],
        [sg.Column([[sg.Text("Preço"), sg.Input(key="Preco")]], pad=(55, 0))],
        [sg.Column([[sg.Text("Quantidade"), sg.Input(key="Quant")]], pad=(23, 0))],
        [sg.Button("Inserir Produto")],
        [
            sg.Table(
                auto_size_columns=False,
                values=[],
                headings=["NOME", "QUANTIDADE", "PREÇO"],
                row_height=20,
                justification="center",
                num_rows=19,
                col_widths=[20, 20, 20],
                key="tabela",
                enable_events=True,
                background_color="white",
                text_color="black",
            )
        ],
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

                janelasys["tabela"].update(produtos)
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
