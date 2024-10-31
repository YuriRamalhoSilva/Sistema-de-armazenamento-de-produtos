import Telas
import conecBD
import userprod.User
import userprod.Produto
import re


class Sistema:

    # USUARIOS

    def Cad_User(email, senha):
        conexao1 = conecBD.conecBD()
        jacad = conexao1.Verificar_email_cadastrado(email)
        conexao1.fechar_conexao()
        if email == "" or senha == "":
            return "sememailousenha"
        elif not Sistema.Val_Email(email):
            return "emailinvalido"
        elif jacad:
            return "emailjaexiste"
        else:
            novo_user = userprod.User.user(email, senha)

            senhau = novo_user.get_senha()
            emailu = novo_user.get_email()

            conexao1 = conecBD.conecBD()

            conexao1.inserir_User(emailu, senhau)

            conexao1.fechar_conexao()

    def Del_User(email):
        conecBD.conecBD.deletar_User(email)

    def Aut_Log(email, senha):
        conexao = conecBD.conecBD()
        if Sistema.Val_Email(email):
            if conexao.Verificar_email_cadastrado(email):

                if conexao.Autenticar_User(email, senha):

                    print("Acesso Liberado!")
                    return "liberado"
                else:
                    print("Acesso Negado!")
                    return "negado"
            else:
                print("Email não cadastrado!")
                return "emailinex"
        else:
            print("Email Inválido")
            return "emailinv"

    def Val_Email(email):
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(regex, email):
            return True
        else:
            return False

    # PRODUTOS

    def Cad_Prod(nome, quant, preco):
        if not nome.strip():
            return "nomevazio"
        elif not quant.strip():
            return "quantvazio"
        elif not preco.strip():
            return "precovazio"
        else:
            novo_produto = userprod.Produto.Produto(nome, quant, preco)
            if novo_produto:
                nomep = novo_produto.get_nome()
                quantp = novo_produto.get_quant()
                precop = novo_produto.get_preco()
                conexao = conecBD.conecBD()
                conexao.Cadastrar_Prod(nomep, quantp, precop)
                conexao.fechar_conexao()

    def Alt_Prod():
        pass

    def Bus_Prod():
        conexao = conecBD.conecBD()
        produtos = conexao.Buscar_Produtos()
        conexao.fechar_conexao()
        return produtos

    def Del_Prod():
        pass
