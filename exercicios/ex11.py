# Faça um programa em Python para gerir sua lista de compras e listar os itens por ordem alfabética.

lista_artigos = []

print("Lista de compras:")
print("Introduza quantos artigos quer introduzir:")
num_artigos = int(input())
print()
for i in range(num_artigos):
    print("Artigo ", i + 1, ":")
    artigo = input()
    artigo = str(artigo)
    lista_artigos.append(artigo)

print()
print("Quer orderar a lista de compras por ordem alfabética? [s] [n]")
escolha = str(input())
escolha = escolha.lower()
print()
if escolha == 'n':
    print("Esta é a lista de compras:")
    print(lista_artigos)
elif escolha == 's':
    print("Lista ordenada alfabeticamente:")
    lista_artigos.sort()
    print(lista_artigos)
else:
    print("Opção indisponível.")