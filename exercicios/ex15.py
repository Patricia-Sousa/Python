# Escreva um programa em Python que receba uma lista de cidades em Portugal digitadas pelo utilizador
# Em seguida, o programa deve filtrar cidades que começam pela letra “a”, e devolve uma nova lista somente com essas cidades
# Apresentar a nova lista no ecrã.

print("Lista de cidades em Portugal")
lista_cidades = []
lista_a = []

print("Quantas cidades quer inserir:")
num = int(input())
for i in range(num):
    print("Cidade:")
    cidade = str(input())
    cidade = cidade.lower()
    lista_cidades.append(cidade)
    if cidade.startswith("a"):
        lista_a.append(cidade)

print("Lista das cidades introduzidas")
print(lista_cidades)
print("O programa filtra as cidades que começam pela letra 'a' ")
if len(lista_a) > 0:
    print(lista_a)
else:
    print("Lista vazia")
