import mysql.connector

conexao = mysql.connector.Connect(
    host='localhost',
    user='root',
password='Mydate2023,,',
database='bancoestudo', 
)

cursor = conexao.cursor()

# CRUD
comando = ''
cursor.execute(comando)
conexao.commit() # Para editar banco de dados



cursor.close()
conexao.close()
