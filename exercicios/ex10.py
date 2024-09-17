# Crie um gestor de tarefas onde seja possível ao utilizador, acrescentar, ver e editar as tarefas diárias.

print("Gestor de tarefas:")
tarefa = []

for i in range(1):
    print("Tarefa", i+1)
    tarefa.append(i+1)
    print("Categoria da tarefa:")
    categoria = str(input())
    tarefa.append(categoria)
    print("Descrição da tarefa:")
    descricao = str(input())
    tarefa.append(descricao)

print("Se quer ver a sua Tarefa introduza [v], se quer editar algum campo introduza [e]")
escolha = str(input())
escolha = escolha.lower()
if escolha == 'v':
    print(tarefa)
elif escolha == 'e':
    print("Qual o campo que pretende editar: categoria [c] ou descrição [d]")
    escolha2 = str(input())
    escolha2 = escolha2.lower()
    if escolha2 == 'c':
        tarefa.pop(1)
        print("Categoria da tarefa:")
        categoria = str(input())
        tarefa.insert(1, categoria)
        print(tarefa)
    elif escolha2 == 'd':
        tarefa.pop(2)
        print("Descrição da tarefa:")
        descricao = str(input())
        tarefa.insert(2, descricao)
        print(tarefa)
    else:
        print("Opção indisponível.")
else:
    print("Opção indisponível.")