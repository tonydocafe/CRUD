import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Altere para seu usuário do MySQL
        password="123456",  # Altere para sua senha do MySQL
        database="clinicmanagerdb"
    )


# Funções de paciente
def criar_paciente():
    conexao = conectar()
    cursor = conexao.cursor()
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    sql = "INSERT INTO pacientes (nome, cpf, telefone, cadastrado) VALUES (%s, %s, %s, NOW())"
    valores = (nome, cpf, telefone)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Paciente cadastrado com sucesso!")
    conexao.close()

def listar_pacientes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, cpf, telefone FROM pacientes")
    for paciente in cursor.fetchall():
        print(paciente)
    conexao.close()

def atualizar_paciente():
    conexao = conectar()
    cursor = conexao.cursor()
    id_paciente = input("ID do paciente: ")
    novo_nome = input("Novo nome: ")
    novo_telefone = input("Novo telefone: ")
    sql = "UPDATE pacientes SET nome = %s, telefone = %s, editado = NOW() WHERE id = %s"
    valores = (novo_nome, novo_telefone, id_paciente)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Paciente atualizado!")
    conexao.close()

def deletar_paciente():
    conexao = conectar()
    cursor = conexao.cursor()
    id_paciente = input("ID do paciente: ")
    sql = "DELETE FROM pacientes WHERE id = %s"
    cursor.execute(sql, (id_paciente,))
    conexao.commit()
    print("Paciente removido!")
    conexao.close()
