# Crie um programa que cria uma lista de compras e depois ordene por ordem alfabética os eleme
# No final diga a quantidade de elementos que a lista contém.

lista = []
print("Lista")
categorias = ['Tarefas', 'Compras', 'Notas']
tarefas = []
compras = []
notas = []
print("Categorias")
print(categorias)
print("Escolha uma categoria")
print(" [t] [c] [n]       Sair [0]")
escolha = str(input())
escolha = escolha.lower()
if escolha == 't':
    print(categorias[0])
    print("TOTAL TAREFAS")
    num_t = int(input())
    for i in range(num_t):
        print("Tarefa")
        tarefa = str(input())
        tarefas.append(tarefa)
elif escolha == 'c':
    print(categorias[1])
    print("TOTAL ARTIGOS")
    num_a = int(input())
    for i in range(num_a):
        print("Artigo")
        artigo = str(input())
        compras.append(artigo)
elif escolha == 'n':
    print(categorias[2])
    print("TOTAL TAREFAS")
    num_n = int(input())
    for i in range(num_n):
        print("Nota")
        nota = str(input())
        notas.append(nota)
elif escolha == '0':
    print("Fim do programa")
else:
    print("Erro")

print("Listas ordenadas alfabeticamente")
print("Tarefas")
print(sorted(tarefas))
print("Compras")
print(sorted(compras))
print("Notas")
print(sorted(notas))

print("Quantidade de elementos")
print("Tarefas")
print(len(tarefas))
print("Compras")
print(len(compras))
print("Notas")
print(len(notas))
