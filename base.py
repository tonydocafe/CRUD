from usuario import *
from paciente import *
from consulta import *
from medico import *
# Menu
def menu():
    while True:
        print("\n1. Criar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("5. Criar Paciente")
        print("6. Listar Pacientes")
        print("7. Atualizar Paciente")
        print("8. Deletar Paciente")
        print("9. Criar Consulta")
        print("10. Listar Consultas")
        print("11. Atualizar Consulta")
        print("12. Deletar Consulta")
        print("13.Listar Consulta do Medico")
        print("14.Criar Medico")
        print("15.Listar Medico")
        print("16. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "5":
            criar_paciente()
        elif opcao == "6":
            listar_pacientes()
        elif opcao == "7":
            atualizar_paciente()
        elif opcao == "8":
            deletar_paciente()
        elif opcao == "9":
            criar_consulta()
        elif opcao == "10":
            listar_consultas()
        elif opcao == "11":
            atualizar_consulta()
        elif opcao == "12":
            deletar_consulta()
        elif opcao == "13":
            listar_consultas_do_medico()
        elif opcao == "14":
            criar_medico()
        elif opcao == "15":
            listar_medicos()
        elif opcao == "16":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
