import mysql.connector
import Sistema


class conecBD:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost", user="root", password="", database="BDcrudpy"
        )
        self.cursor1 = self.conexao.cursor()

    # USUARIOS

    def Verificar_email_cadastrado(self, email):
        try:

            sql = "SELECT email FROM Table_Users WHERE email = %s"
            self.cursor1.execute(sql, (email,))
            resultado = self.cursor1.fetchone()
            if resultado:
                return True  # E-mail já existe
            else:
                return False  # E-mail não existe
        except mysql.connector.Error as err:
            print(f"Erro ao verificar email: {err}")

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

        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return False

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

    def Autenticar_User(self, email, senha):
        try:
            if self.conexao.is_connected():
                self.cursor1 = self.conexao.cursor(dictionary=True)

            valores = (email,)
            sql = "SELECT email,senha FROM table_users WHERE email = %s;"

            if self.conexao.is_connected():
                print("Conectou")
            else:
                print("Não Conectou")

            self.cursor1.execute(sql, valores)

            dados = self.cursor1.fetchone()

            if dados and dados["senha"] == senha:
                return True
            else:
                return False

        except mysql.connector.Error as err:
            print(f"Erro ao encontrar usuário: {err}")

    # PRODUTOS

    def Cadastrar_Prod(self, nome, quant, preco):

        try:
            valores = (nome, quant, preco)

            sql = "Insert into table_products (nome,quantidade,preco) values (%s,%s,%s)"
            self.cursor1.execute(sql, valores)

            if self.conexao.is_connected():
                print("Conectou!")
            else:
                print("Não Conectou!")

            self.conexao.commit()
            print("Dados do produto foram inseridos!")

        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return False

    def Buscar_Produtos(self):
        try:
            sql = "SELECT ID_produto,nome,quantidade,preco FROM table_products"

            self.cursor1.execute(sql)

            print("Os produtos foram encontrados!")
            busca = self.cursor1.fetchall()
            return busca
        except mysql.connector.Error as err:
            print(err)

    def Delete_Produtos(self, id):
        try:
            valores = (id,)
            sql = "SELECT nome FROM table_products WHERE ID_produto = %s"
            self.cursor1.execute(sql, valores)
            prodDel = self.cursor1.fetchone()

            sql = "DELETE FROM table_products WHERE ID_produto = %s"

            self.cursor1.execute(sql, valores)

            if self.conexao.is_connected():
                print("Conectou")
            else:
                print("Não conectou")

            self.conexao.commit()

            if self.cursor1.rowcount > 0:
                print(f"Produto {prodDel} deletado com sucesso do banco de dados!")
                return True
            else:
                print(f"Produto {prodDel} nao foi encontrado no banco de dados!")
                return False

        except mysql.connector.Error as err:
            print(err)

    def Update_Produtos(self, id, nome, quant, preco):
        pass

    def fechar_conexao(self):
        # Função para fechar o cursor e a conexão quando for necessário
        self.cursor1.close()
        self.conexao.close()
        print("Conexão e cursor foram fechados.")
