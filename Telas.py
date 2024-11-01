import PySimpleGUI as sg  # Importação da biblioteca de interface e apelidando de sg
import Sistema


def popup_custom(mensagem):  # Função que atribui uma bind ao popup do sistema todo
    layout = [[sg.Text(mensagem)], [sg.Button("OK", bind_return_key=True)]]

    popup_window = sg.Window("Atenção!", layout, modal=True, finalize=True)
    popup_window.bind("<Return>", "_Enter")  # Vincula a tecla Enter ao evento _Enter

    while True:
        evento, _ = popup_window.read()
        if evento in (sg.WIN_CLOSED, "OK", "_Enter"):  # Fecha com Enter ou botão OK
            break

    popup_window.close()


def popup_custom_confirm(
    mensagem,
):  # Função que atribui uma bind ao popup do sistema todo
    layout = [
        [sg.Text(mensagem)],
        [
            sg.Column(
                [
                    [
                        sg.Button("Sim", bind_return_key=True, size=(5, 1)),
                        sg.Button("Não", bind_return_key=True, size=(5, 1)),
                    ]
                ],
                justification="center",
            )
        ],
    ]

    popup_window = sg.Window("Atenção!", layout, modal=True, finalize=True)
    popup_window.bind("<Return>", "_Enter")  # Vincula a tecla Enter ao evento Return
    popup_window.bind("<Escape>", "_Esc")  # Vincula a tecla Esc ao evento Escape

    while True:
        evento, _ = popup_window.read()
        if evento in ("Sim", "_Enter"):
            popup_window.close()
            return "Sim"
        elif evento in ("Não", "_Esc", sg.WIN_CLOSED):
            popup_window.close()
            return "Não"


def Form_Preco(preco):
    return f"R$  {preco:.2f}"


def TelaLogin():  # Função de funcionamento da interface de login

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
        [sg.Button("Logar", bind_return_key=True), sg.Button("Sair")],
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
                popup_custom("Acesso Negado!\nA senha está incorreta!")
            elif retorno == "emailinex":
                popup_custom(
                    "Erro!\nNão foi possivel encontrar um usuário com esse E-mail cadastrado no sistema!"
                )
            elif retorno == "emailinv":
                popup_custom(
                    "Erro!\nDigite um E-mail válido!\nExemplo: E-mailexemplo@exemplo.com"
                )

        if evento == "Cadastre-se":
            janelalog.close()
            return "Cadastre-se"


def TelaCadUser():  # Função de funcionamento da interface de cadastro de novos usuários
    layout = [
        [sg.Text("Coloque seu email e senha!")],
        [sg.Text("Email ")],
        [sg.Input(key="Email")],
        [sg.Text("Senha ")],
        [sg.Input(key="Senha", password_char="*")],
        [sg.Text("Confirme sua senha")],
        [sg.Input(key="confsenha", password_char="*")],
        [sg.Button("Cadastrar", bind_return_key=True)],
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
                popup_custom("Erro\nA confirmação da senha não foi validada!")
            else:
                retorno = Sistema.Sistema.Cad_User(email, senha)

                if retorno == "sememailousenha":
                    popup_custom("Erro\nErro ao Cadastrar, digite seu usuário e senha!")
                elif retorno == "emailinvalido":
                    popup_custom(
                        "Erro\nDigite um E-mail válido, por exemplo: E-mailexemplo@exemplo.com"
                    )
                elif retorno == "emailjaexiste":
                    popup_custom(
                        "Erro\nUsuário já cadastrado no sistema com esse E-Mail!"
                    )
                else:
                    popup_custom("Cadastro Concluído!\nUsuário cadastrado com sucesso!")


def TelaSys():  # Função de funcionamento da Inserção de produtos e sua interface
    produtos = Sistema.Sistema.Bus_Prod()
    res_largura, res_altura = sg.Window.get_screen_size()
    jan_largura, jan_altura = 600, 620
    px = (res_largura - jan_largura) // 2
    py = (res_altura - jan_altura) // 2

    layout = [
        [sg.Text("Cadastro de Produtos!")],
        [
            sg.Column(
                [[sg.Text("Nome"), sg.Input(key="Nome", enable_events=True)]],
                pad=(55, 0),
            )
        ],
        [
            sg.Column(
                [[sg.Text("Quantidade"), sg.Input(key="Quant", enable_events=True)]],
                pad=(23, 0),
            )
        ],
        [
            sg.Column(
                [[sg.Text("Preço"), sg.Input(key="Preco", enable_events=True)]],
                pad=(55, 0),
            )
        ],
        [
            sg.Column(
                [
                    [
                        sg.Button(
                            "Inserir Produto", bind_return_key=True, size=(13, 1)
                        ),
                        sg.Button("Deletar Produto", size=(13, 1)),
                        sg.Button("Editar Produto", size=(13, 1)),
                        sg.Button("Auto-Insert", size=(13, 1)),
                    ]
                ],
                pad=(20, 4),
                justification="center",
            )
        ],
        [
            sg.Table(
                auto_size_columns=False,
                values=[
                    [id, nome, quant, Form_Preco(preco)]
                    for id, nome, quant, preco in produtos
                ],
                headings=["ID", "NOME", "QUANTIDADE", "PREÇO"],
                row_height=20,
                select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                justification="center",
                num_rows=20,
                col_widths=[10, 20, 15, 15],
                key="tabela",
                enable_events=True,
                background_color="white",
                text_color="black",
            )
        ],
        [sg.Button("Deslogar")],
    ]
    janelasys = sg.Window(
        "Sistema", layout, size=(jan_largura, jan_altura), location=(px, py)
    )

    while True:

        evento, valores = janelasys.read()
        if evento == sg.WIN_CLOSED:
            janelasys.close()
            return None

        if evento == "Preco":
            digitado = valores["Preco"]
            if not (
                digitado.replace(",", "", 1).replace(".", "", 1).isdigit()
                and digitado.count(",") <= 1
                and digitado.count(".") <= 1
            ):
                janelasys["Preco"].update(digitado[:-1])

        if evento == "Quant":
            digitado = valores["Quant"]
            if not digitado.isdigit():
                janelasys["Quant"].update(digitado[:-1])

        if evento == "Inserir Produto":
            nome, quant, preco = valores["Nome"], valores["Quant"], valores["Preco"]
            retorno = Sistema.Sistema.Cad_Prod(nome, quant, preco)
            if (
                retorno == "nomevazio"
                or retorno == "precovazio"
                or retorno == "quantvazio"
            ):
                popup_custom(
                    "Erro\nNão foi possivel cadastrar um produto!\nNão deixe nenhum campo vazio!"
                )
            else:
                produtos = Sistema.Sistema.Bus_Prod()
                janelasys["tabela"].update(
                    [id, nome, quant, Form_Preco(preco)]
                    for id, nome, quant, preco in produtos
                )
                popup_custom("Inserido!\nProduto inserido com sucesso!")
                janelasys["Nome"].update("")
                janelasys["Quant"].update("")
                janelasys["Preco"].update("")

        if evento == "Deletar Produto":
            linhaselec = valores["tabela"]  # Pega a linha selecionada
            if linhaselec:
                dadoslinha = produtos[linhaselec[0]]
                retornopop = popup_custom_confirm(
                    f"Tem certeza que você quer deletar esse produto?\n{dadoslinha}"
                )
                if retornopop == "Sim":
                    retornosis = Sistema.Sistema.Del_Prod(dadoslinha[0])
                    if retornosis:
                        popup_custom(
                            f"Produto {dadoslinha[1]} foi deletado do sistema!"
                        )
                        produtos = Sistema.Sistema.Bus_Prod()
                        janelasys["tabela"].update(
                            [id, nome, quant, Form_Preco(preco)]
                            for id, nome, quant, preco in produtos
                        )

                    elif not retornosis:
                        popup_custom(f"Produto {dadoslinha[1]} nao foi encontrado!")

                elif retornopop == "Não":
                    pass

        if evento == "Editar Produto":
            pass

        if evento == "Auto-Insert":
            pass

        elif evento == "Deslogar":
            retorno = popup_custom_confirm("Você tem certeza que quer deslogar?")
            if retorno == "Sim":
                janelasys.close()
                return "Deslogar"
            elif retorno == "Não":
                continue


# Loop principal que executa as telas em ordem
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
