import Telas
import conecBD
import userprod.User
import userprod.Produto
import re


class Sistema:

    # USUARIOS

    def Cad_User(email, senha):
        if email == "" or senha == "":
            return ("sememailousenha", None)
        elif Sistema.Val_Email(email) == False:
            return ("emailinvalido", None)
        else:
            novo_user = userprod.User.user(email, senha)
            v1, v2 = novo_user.retorna_user()
            conexao1 = conecBD.conecBD()

            insertsuceful, erro = conexao1.inserir_User(v1, v2)

            if not insertsuceful:
                return ("errobanco", erro)

            conexao1.fechar_conexao()

    def Del_User(email):
        conecBD.conecBD.deletar_User(email)

    def Ler_User():

        # parei aki -----------------
        pass

    def Val_Email(email):
        regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(regex, email):
            return True
        else:
            return False

    # PRODUTOS

    def Cad_Prod():
        pass

    def Alt_Prod():
        pass

    def Lis_Prod():
        pass

    def Del_Prod():
        pass
