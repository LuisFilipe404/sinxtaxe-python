tarefas = []


def adicionar_tarefa(nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"\nTarefa {nome_tarefa} adicionada com sucesso!\n")
    return


def ver_tarefas():
    print("\nLista de tarefas:\n")

    for indice, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["completada"] else "✗"
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice + 1}, [{status}] {nome_tarefa}")

    print("\n")
    return


def atualizar_nome_tarefa(indice_tarefa, novo_nome_tarefa):

    if indice_tarefa >= 0 and indice_tarefa < len(tarefas):
        tarefas[indice_tarefa]["tarefa"] = novo_nome_tarefa

        print(
            f"Tarefa {tarefas[indice_tarefa]['tarefa']} atualizada para {novo_nome_tarefa}"
        )
    else:
        print("Tarefa não encontrada")

    return


def completar_tarefa(indice_tarefa):
    if indice_tarefa >= 0 and indice_tarefa < len(tarefas):
        tarefas[indice_tarefa]["completada"] = True
        print(f"Tarefa {tarefas[indice_tarefa]['tarefa']} completada")
    else:
        print("Tarefa não encontrada")

    return


def deletar_tarefas_completadas():
    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)

    print("Tarefas completadas foram deletadas")
    return


while True:
    print("Gerenciador de listas de tarefas")
    print("1. Adicionar uma tarefa")
    print("2. Ver tarefa")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(nome_tarefa)
    elif escolha == "2":
        ver_tarefas()
    elif escolha == "3":
        ver_tarefas()
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(int(indice_tarefa) - 1, novo_nome_tarefa)
    elif escolha == "4":
        ver_tarefas()
        indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
        completar_tarefa(int(indice_tarefa) - 1)
    elif escolha == "5":
        deletar_tarefas_completadas()
    elif escolha == "6":
        break

print("Programa finalizado")
