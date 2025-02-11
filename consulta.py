import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Altere para seu usuário do MySQL
        password="123456",  # Altere para sua senha do MySQL
        database="clinicmanagerdb"
    )


# Funções de consulta
def criar_consulta():
    conexao = conectar()
    cursor = conexao.cursor()
    
    medico_id = input("ID do médico: ")
    cursor.execute("SELECT id FROM medicos WHERE id = %s", (medico_id,))
    if not cursor.fetchone():
        print("Médico inexistente!")
        return

    
    paciente_id = input("ID do paciente: ")
    
    cursor.execute("SELECT id FROM pacientes WHERE id = %s", (paciente_id,))
    if not cursor.fetchone():
        print("Paciente inexistente!")
        return
    descricao = input("Descrição da consulta: ")
    data_agendamento = input("Data da consulta (YYYY-MM-DD HH:MM:SS): ")
    
    sql = "INSERT INTO consultas (medico_id, paciente_id, descricao, data_agendamento, cadastrado) VALUES (%s, %s, %s, %s, NOW())"
    valores = (medico_id, paciente_id, descricao, data_agendamento)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Consulta cadastrada com sucesso!")
    conexao.close()

def listar_consultas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, medico_id, paciente_id, descricao, data_agendamento FROM consultas")
    for consulta in cursor.fetchall():
        print(consulta)
    conexao.close()

def atualizar_consulta():
    conexao = conectar()
    cursor = conexao.cursor()
    id_consulta = input("ID da consulta: ")
    nova_descricao = input("Nova descrição: ")
    nova_data_agendamento = input("Nova data da consulta (YYYY-MM-DD HH:MM:SS): ")
    sql = "UPDATE consultas SET descricao = %s, data_agendamento = %s, editado = NOW() WHERE id = %s"
    valores = (nova_descricao, nova_data_agendamento, id_consulta)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Consulta atualizada!")
    conexao.close()

def deletar_consulta():
    conexao = conectar()
    cursor = conexao.cursor()
    id_consulta = input("ID da consulta: ")
    sql = "DELETE FROM consultas WHERE id = %s"
    cursor.execute(sql, (id_consulta,))
    conexao.commit()
    print("Consulta removida!")
    conexao.close()

# Função para listar todas as consultas de um médico
def listar_consultas_do_medico():
    medico_id = input("Informe o ID do médico: ")
    conexao = conectar()
    cursor = conexao.cursor()

    # Consulta SQL para listar as consultas de um médico específico
    sql = """
    SELECT consultas.id, pacientes.nome AS paciente, consultas.data_agendamento, consultas.descricao
    FROM consultas
    JOIN pacientes ON consultas.paciente_id = pacientes.id
    WHERE consultas.medico_id = %s
    """
    cursor.execute(sql, (medico_id,))
    consultas = cursor.fetchall()

    if consultas:
        print(f"Consultas do Médico {medico_id}:")
        for consulta in consultas:
            print(f"ID Consulta: {consulta[0]}, Paciente: {consulta[1]}, Data: {consulta[2]}, Descrição: {consulta[3]}")
    else:
        print(f"O médico com ID {medico_id} não tem consultas agendadas.")

    conexao.close()