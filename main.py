tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a tarefa a ser adicionada: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def remover_tarefa():
    if not tarefas:
        print("A lista de tarefas está vazia.")
        return

    print("Lista de tarefas:")
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1}. {tarefa}")

    opcao = input("Digite o índice da tarefa a ser removida ou o nome da tarefa: ")
    if opcao.isdigit():
        index = int(opcao) - 1
        if 0 <= index < len(tarefas):
            tarefa_removida = tarefas.pop(index)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Índice inválido.")
    else:
        if opcao in tarefas:
            tarefas.remove(opcao)
            print(f"Tarefa '{opcao}' removida com sucesso!")
        else:
            print("Tarefa não encontrada.")

def listar_tarefas():
    if not tarefas:
        print("A lista de tarefas está vazia.")
    else:
        print("Lista de tarefas:")
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1}. {tarefa}")

def marcar_como_concluida():
    if not tarefas:
        print("A lista de tarefas está vazia.")
        return

    print("Lista de tarefas:")
    for i, tarefa in enumerate(tarefas):
        print(f"{i + 1}. {tarefa}")

    opcao = input("Digite o índice da tarefa concluída: ")
    if opcao.isdigit():
        index = int(opcao) - 1
        if 0 <= index < len(tarefas):
            tarefa = tarefas[index]
            print(f"Tarefa '{tarefa}' marcada como concluída!")
            tarefas.pop(index)
        else:
            print("Índice inválido.")
    else:
        print("Opção inválida.")

while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Listar Tarefas")
    print("4. Marcar Tarefa como Concluída")
    print("5. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        remover_tarefa()
    elif opcao == "3":
        listar_tarefas()
    elif opcao == "4":
        marcar_como_concluida()
    elif opcao == "5":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")