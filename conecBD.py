import mysql.connector 
    
conexao = mysql.connector.connect(
      host= 'localhost',
      user= 'root',
      password= '',
      database= 'BDcrudpy')
cursor = conexao.cursor()
class conecBD:
   
    def inserir():
        cursor.execute("")
        pass

    def deletar():
        cursor.execute("")
        pass

    def alterar():
        cursor.execute("")
        pass

    def select():
        cursor.execute("")
        pass

