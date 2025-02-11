import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="clinicmanagerdb"
    )

def criar_medico():
    conexao = conectar()
    cursor = conexao.cursor()
    
    # Coletar dados do usuário
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    login = input("Login: ")
    password = input("Senha: ")
    crm = input("CRM: ")  # O CRM é específico do médico

    try:
        # 1. Inserir na tabela usuarios
        sql_usuario = """
        INSERT INTO usuarios (nome, cpf, telefone, email, login, password, tipo_usuario)
        VALUES (%s, %s, %s, %s, %s, %s, 'Medico')
        """
        valores_usuario = (nome, cpf, telefone, email, login, password)
        cursor.execute(sql_usuario, valores_usuario)
        conexao.commit()

        # 2. Pegar o ID gerado
        id_medico = cursor.lastrowid

        # 3. Inserir o CRM na tabela medicos
        sql_medico = "INSERT INTO medicos (id, crm) VALUES (%s, %s)"
        valores_medico = (id_medico, crm)
        cursor.execute(sql_medico, valores_medico)
        conexao.commit()

        print("Médico cadastrado com sucesso!")

    except mysql.connector.Error as erro:
        print(f"Erro ao cadastrar médico: {erro}")
        conexao.rollback()

    finally:
        conexao.close()

def listar_medicos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT u.id, u.nome, u.cpf, u.telefone, u.email, m.crm
    FROM usuarios u
    INNER JOIN medicos m ON u.id = m.id
    """
    
    cursor.execute(sql)
    medicos = cursor.fetchall()

    if medicos:
        print("Médicos cadastrados:")
        for medico in medicos:
            print(f"ID: {medico[0]}, Nome: {medico[1]}, CPF: {medico[2]}, Telefone: {medico[3]}, Email: {medico[4]}, CRM: {medico[5]}")
    else:
        print("Nenhum médico cadastrado.")

    conexao.close()
