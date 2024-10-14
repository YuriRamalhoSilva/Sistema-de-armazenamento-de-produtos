import mysql.connector 
    
conexao = mysql.connector.connect(
      host= 'localhost',
      user= 'root',
      password= '',
      database= 'BDcrudpy')
cursor = conexao.cursor()


class conecBD:
   
    def inserir_User(email,senha):
        valores = (email,senha)
        
        sql = 'Insert into Table_Users (email,senha) values (%s,%s)'
        
        cursor.execute(sql,valores)
        
        if conexao.is_connected():
         print("Conectou")
        else:
         print("Não Conectou")

        conexao.commit()
        cursor.close()
        conexao.close()     
        

    def deletar_User(email):
    
     try:
            valores =(email,)
            sql = ("DELETE FROM Table_Users WHERE email = %s")
        
            cursor.execute(sql,valores)

            if conexao.is_connected():
                print("Conectou")
            else:
                print("Não Conectou")

            conexao.commit()

            if cursor.rowcount > 0:
                print(f"User {email} deletado com sucesso do banco de dados!")
            else:
                print(f"User {email} nao foi encontrado no banco de dados!")

     except mysql.connector.Error as err:
                print(f"Erro ao deletar usuário: {err}")
     finally:
    
        cursor.close()
        conexao.close()
        

    def alterar():
        cursor.execute("")
        pass

    def select():
        cursor.execute("")
        pass

    
    deletar_User("email2@gmail.com")

