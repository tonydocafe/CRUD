import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="123456",  
        database="clinicmanagerdb"
    )

# Funções de usuário
def criar_usuario():
    conexao = conectar()
    cursor = conexao.cursor()
    nome = input("Nome: ")
    cpf = input("CPF: ")
    login = input("Login: ")
    password = input("Senha: ")
    tipo_usuario = input("Tipo (Medico, Atendente, ADMIN): ")
    sql = "INSERT INTO usuarios (nome, cpf, login, password, tipo_usuario, cadastrado) VALUES (%s, %s, %s, %s, %s, NOW())"
    valores = (nome, cpf, login, password, tipo_usuario)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Usuário cadastrado com sucesso!")
    conexao.close()

def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, cpf, login, tipo_usuario FROM usuarios")
    for usuario in cursor.fetchall():
        print(usuario)
    conexao.close()

def atualizar_usuario():
    conexao = conectar()
    cursor = conexao.cursor()
    id_usuario = input("ID do usuário: ")
    novo_nome = input("Novo nome: ")
    sql = "UPDATE usuarios SET nome = %s, editado = NOW() WHERE id = %s"
    valores = (novo_nome, id_usuario)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Usuário atualizado!")
    conexao.close()

def deletar_usuario():
    conexao = conectar()
    cursor = conexao.cursor()
    id_usuario = input("ID do usuário: ")
    sql = "DELETE FROM usuarios WHERE id = %s"
    cursor.execute(sql, (id_usuario,))
    conexao.commit()
    print("Usuário removido!")
    conexao.close()


