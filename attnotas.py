def menu():
    print("\nMenu:")
    print("1 - Agendar Atendimento")
    print("2 - Chamar Próximo Paciente")
    print("3 - Excluir Agendamentos")
    print("4 - Ver Lista de Pacientes")
    print("5 - Sair do Programa")

prioridades = {
    1: "Crítico",
    2: "Grave",
    3: "Leve"
}

fila_prioridade = []

def ordenar_fila():
    fila_prioridade.sort(key=lambda paciente: paciente[0])

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do paciente: ")
        print("Escolha a gravidade (1: Crítico, 2: Grave, 3: Leve): ")
        try:
            gravidade_num = int(input())
            if gravidade_num not in prioridades:
                print("Gravidade inválida. Tente novamente.")
            else:
                enfermidade = prioridades[gravidade_num]
                prioridade = gravidade_num
                fila_prioridade.append((prioridade, nome))
                ordenar_fila()
                print(f"Paciente {nome} com gravidade {enfermidade} agendado.")
        except ValueError:
            print("Por favor, digite um número válido para gravidade.")

    elif opcao == "2":
        if fila_prioridade:
            prioridade, nome = fila_prioridade.pop(0)
            print(f"Chamando paciente: {nome} (Prioridade: {prioridade})")
        else:
            print("Nenhum paciente na fila.")

    elif opcao == "3":
        if fila_prioridade:
            print("Excluindo todos os agendamentos...")
            while fila_prioridade:
                prioridade, nome = fila_prioridade.pop(0)
                print(f"Paciente {nome} (Prioridade: {prioridade}) não atendido.")
        else:
            print("Nenhum paciente para excluir.")

    elif opcao == "4":
        if fila_prioridade:
            print("Lista de pacientes na fila de prioridade:")
            for prioridade, nome in fila_prioridade:
                gravidade = prioridades[prioridade]
                print(f"Paciente: {nome}, Gravidade: {gravidade}, Prioridade: {prioridade}")
        else:
            print("A fila de pacientes está vazia.")

    elif opcao == "5":
        print("Saindo do programa. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
