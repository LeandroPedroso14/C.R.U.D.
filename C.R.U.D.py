import mysql.connector

conexao = mysql.connector.Connect(
    host='localhost',
    user='root',
password='Mydate2023,,',
database='bancoestudo', 
)

cursor = conexao.cursor()

# CRUD
comando = 'INSERT INTO vendas '
cursor.execute(comando)
conexao.commit() # Para editar banco de dados.
resultado = cursor.fetchall() # Ler o banco de dados.



cursor.close()
conexao.close()
