import PySimpleGUI as sg  # Importação da biblioteca de interface e apelidando de sg
import CadAuto.autoinsert
import Sistema
import csv
import CadAuto


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
                        sg.Button("Não", bind_return_key=True, size=(5, 1)),
                        sg.Button("Sim", bind_return_key=True, size=(5, 1)),
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
        [sg.Push(), sg.Text("Faça seu Login!"), sg.Push()],
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
        [
            sg.Text("    "),
            sg.Button("Logar", bind_return_key=True),
            sg.Button("Sair"),
        ],
        [sg.Push(), sg.Text("Ainda não está cadastrado?")],
        [sg.Push(), sg.Button("Cadastre-se")],
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
        [
            sg.Column(
                [[sg.Button("Cadastrar", bind_return_key=True), sg.Button("Voltar")]]
            )
        ],
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
        [sg.Push(), sg.Text("Cadastro de Produtos!"), sg.Push()],
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
        [
            sg.Column(
                [
                    [
                        sg.Button("Deslogar"),
                        sg.Text(
                            "                                                                                             "
                        ),
                        sg.Button("Atualizar Tabela"),
                    ]
                ],
            )
        ],
    ]
    janelasys = sg.Window(
        "Sistema", layout, size=(jan_largura, jan_altura), location=(px - 300, py)
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

            linhaselec = valores["tabela"]  # Pega a linha selecionada
            if linhaselec:
                dadoslinha = produtos[linhaselec[0]]
                if TelaEditProd(dadoslinha):
                    produtos = Sistema.Sistema.Bus_Prod()
                    janelasys["tabela"].update(
                        [id, nome, quant, Form_Preco(preco)]
                        for id, nome, quant, preco in produtos
                    )
            else:
                popup_custom("Selecione um produto da tabela para editar!")

        if evento == "Auto-Insert":
            TelaAnex()
            pass

        if evento == "Deslogar":
            retorno = popup_custom_confirm("Você tem certeza que quer deslogar?")
            if retorno == "Sim":
                janelasys.close()
                return "Deslogar"
            elif retorno == "Não":
                continue

        if evento == "Atualizar Tabela":
            produtos = Sistema.Sistema.Bus_Prod()
            janelasys["tabela"].update(
                [id, nome, quant, Form_Preco(preco)]
                for id, nome, quant, preco in produtos
            )


def TelaEditProd(dadoslinha):

    layout = [
        [sg.Text(f"Edição do Produto {dadoslinha[1]}")],
        [
            sg.Column(
                [
                    [
                        sg.Text("Nome"),
                        sg.Input(
                            key="NovoNome",
                            default_text=f"{dadoslinha[1]}",
                            enable_events=True,
                        ),
                    ]
                ],
                justification="right",
            )
        ],
        [
            sg.Column(
                [
                    [
                        sg.Text("Quantidade"),
                        sg.Input(
                            key="NovoQuant",
                            default_text=f"{dadoslinha[2]}",
                            enable_events=True,
                        ),
                    ]
                ],
                justification="right",
            )
        ],
        [
            sg.Column(
                [
                    [
                        sg.Text("Preço"),
                        sg.Input(
                            key="NovoPreco",
                            default_text=f"{dadoslinha[3]}",
                            enable_events=True,
                        ),
                    ]
                ],
                justification="right",
            )
        ],
        [
            sg.Column(
                [[sg.Button("Confirmar", bind_return_key=True), sg.Button("Cancelar")]]
            )
        ],
    ]

    janedit = sg.Window("Editar", layout, location=(1336, 420))

    while True:
        evento, valores = janedit.read()

        if evento in ("Cancelar", sg.WIN_CLOSED):
            janedit.close()
            return None

        if evento == "NovoPreco":
            digitado = valores["NovoPreco"]
            if not (
                digitado.replace(",", "", 1).replace(".", "", 1).isdigit()
                and digitado.count(",") <= 1
                and digitado.count(".") <= 1
            ):
                janedit["NovoPreco"].update(digitado[:-1])

        if evento == "NovoQuant":
            digitado = valores["NovoQuant"]
            if not digitado.isdigit():
                janedit["NovoQuant"].update(digitado[:-1])

        if evento == "Confirmar":
            retornopop = popup_custom_confirm(
                f"Tem certeza que quer alterar o produto {dadoslinha[1]} ?"
            )
            if retornopop == "Sim":
                id = dadoslinha[0]
                NovoNome, NovoQuant, NovoPreco = (
                    valores["NovoNome"],
                    valores["NovoQuant"],
                    valores["NovoPreco"],
                )
                retornoedit = Sistema.Sistema.Alt_Prod(
                    id, NovoNome, NovoQuant, NovoPreco
                )
                if retornoedit == "nomevazio":
                    popup_custom("Digite o novo nome do produto para alterar!")
                elif retornoedit == "quantvazio":
                    popup_custom("Digite a nova quantidade do produto para alterar!")
                elif retornoedit == "precovazio":
                    popup_custom("Digite o novo preço do produto para aterar!")
                elif retornoedit == "Erro":
                    popup_custom("Erro\nAlgo de errado aconteceu :(")
                elif retornoedit == "AltConf":
                    popup_custom(
                        f"Produto {dadoslinha} alterado para {NovoNome,NovoQuant,NovoPreco} !"
                    )
                    janedit.close()
                    return True

            elif retornopop == "Não":
                continue


def TelaAnex():
    res_largura, res_altura = sg.Window.get_screen_size()
    jan_largura, jan_altura = 600, 620
    px = (res_largura - jan_largura) // 2
    py = (res_altura - jan_altura) // 2
    layout = [
        [
            sg.Text("Anexar um arquivo CSV:"),
            sg.Input(),
            sg.FileBrowse(file_types=(("CSV Files", "*.csv"),)),
        ],
        [sg.Button("Carregar Arquivo"), sg.Button("Fechar")],
        [
            sg.Table(
                auto_size_columns=False,
                values=[[]],
                headings=["NOME", "QUANTIDADE", "PREÇO"],
                row_height=20,
                select_mode=sg.TABLE_SELECT_MODE_BROWSE,
                justification="center",
                num_rows=23,
                col_widths=[20, 20, 20],
                key="-TABELA-",
                enable_events=True,
                background_color="white",
                text_color="black",
                visible=False,
            )
        ],
        [
            sg.Text(
                "ATENÇÃO: O botao 'Inserir Automaticamente' insere esses dados na tabela principal!",
                key="aviso",
                visible=False,
                enable_events=True,
            )
        ],
        [sg.Button("Inserir Automaticamente", visible=False, enable_events=True)],
    ]

    jananex = sg.Window(
        "Visualizador de Arquivo CSV",
        layout,
        size=(jan_largura, jan_altura),
        location=(px + 300, py),
        modal=True,
    )

    while True:
        evento, valores = jananex.read()

        if evento == sg.WINDOW_CLOSED or evento == "Fechar":
            break

        if evento == "Carregar Arquivo":
            caminho_arquivo = valores[0]
            if caminho_arquivo:
                try:
                    # Lê o arquivo CSV usando a biblioteca csv
                    with open(caminho_arquivo, newline="") as arquivo:
                        leitor = csv.reader(arquivo)
                        dados_arquivo = list(leitor)

                        # Ignora a primeira linha se for cabeçalho e carrega o restante dos dados
                        dados_linha = (
                            dados_arquivo[1:] if len(dados_arquivo) > 1 else []
                        )

                        # Atualiza a tabela com os dados do CSV
                        jananex["-TABELA-"].update(values=dados_linha, visible=True)
                        jananex["Inserir Automaticamente"].update(visible=True)
                        jananex["aviso"].update(visible=True)

                except Exception as e:
                    sg.popup_error("Erro ao carregar o arquivo:", e)

        if evento == "Inserir Automaticamente":
            # Copiar o arquivo.csv pra pasta CadAuto
            CadAuto.autoinsert.autoinsert.copy_file_to_CadAuto(caminho_arquivo)
            # Chamar o metodo do auto insert

            break
    jananex.close()


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
