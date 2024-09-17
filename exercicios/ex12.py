# Crie um programa que receba os nomes dos programadores da sua empresa e acrescente o seu nome ao final da lista.

lista = []

print("Introduza o seu nome:")
nome = str(input())

print("Quantos programadores existem na sua empresa:")
num_prog = int(input())
for i in range(num_prog):
    print("Introduza o nome do programador:")
    nome2 = str(input())
    lista.append(nome2)

lista.append(nome)
print("A lista introduzida:")
print(lista)
