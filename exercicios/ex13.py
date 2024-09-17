# Elabore um programa que recebe uma lista das disciplinas de uma escola e ordene
# os elementos da mesma por ordem alfabética.

print("Lista de disciplinas")
lista = []

print("Quantas disciplinas quer inserir:")
num_dis = int(input())
for i in range(num_dis):
    print("Nome Disciplina:")
    disciplina = str(input())
    lista.append(disciplina)

lista.sort()
print("A lista ordenada alfabeticamente:")
print(lista)