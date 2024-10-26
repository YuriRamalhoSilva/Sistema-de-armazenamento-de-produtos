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
            v1, v2 = novo_user.retorna_user()
            conexao1 = conecBD.conecBD()

            conexao1.inserir_User(v1, v2)

            conexao1.fechar_conexao()

    def Del_User(email):
        conecBD.conecBD.deletar_User(email)

    def Aut_Log(email,senha):
        conexao = conecBD.conecBD()
        if conexao.Verificar_email_cadastrado(email):
            
            if conexao.Autenticar_User(email,senha):
                
                print("Acesso Liberado!")
                return "liberado"
            else:
                print("Acesso Negado!")
                return "negado"
        else:
            print("Email não cadastrado!")
            return "emailinex"


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

Sistema.Aut_Log('emailexemplo@gmail.com', 'senhaexemplo123')
