import mysql.connector
import Sistema


class conecBD:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost", user="root", password="", database="BDcrudpy"
        )
        self.cursor1 = self.conexao.cursor()

    def inserir_User(self, email, senha):
        try:

            valores = (email, senha)

            sql = "Insert into Table_Users (email,senha) values (%s,%s)"

            self.cursor1.execute(sql, valores)

            if self.conexao.is_connected():
                print("Conectou")
            else:
                print("Não Conectou")

            self.conexao.commit()
            print("Conectou e inseriu o usuário com sucesso!")
            return (True, None)

        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return (False, err)

        finally:
            print("fim")

    def deletar_User(self, email):

        try:

            valores = (email,)
            sql = "DELETE FROM Table_Users WHERE email = %s"

            self.cursor1.execute(sql, valores)

            if self.conexao.is_connected():
                print("Conectou")
            else:
                print("Não Conectou")

            self.conexao.commit()

            if self.cursor1.rowcount > 0:
                print(f"User {email} deletado com sucesso do banco de dados!")
            else:
                print(f"User {email} nao foi encontrado no banco de dados!")

        except mysql.connector.Error as err:
            print(err)
        finally:
            print("Deu")

    def buscar_User(self, email):
        try:

            valores = (email,)

            sql = "SELECT email,senha FROM table_users WHERE email = %s;"
            if self.conexao.is_connected():
                print("Conectou")
            else:
                print("Não Conectou")
            self.cursor1.execute(sql, valores)

            dados = self.cursor1.fetchall()
            if dados == []:
                print("Erro, usuário não existe!")
            else:
                print(dados)
                return dados
        except mysql.connector.Error as err:
            print(f"Erro ao encontrar usuário: {err}")
        finally:
            print(f"O usuario {email} foi encontrado no banco e retornado ao programa!")

    def fechar_conexao(self):
        # Função para fechar o cursor e a conexão quando for necessário
        self.cursor1.close()
        self.conexao.close()
        print("Conexão e cursor foram fechados.")
