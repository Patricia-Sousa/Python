# Escreva um programa em Python que encontre o maior e menor elemento de uma lista,
# onde os elementos da lista são pedidos ao utilizador.

print("Insira uma lista de números inteiros:")
lista = []
print("Insira o número total de elementos da lista:")
num_total = int(input())
for i in range(num_total):
    num = int(input())
    lista.append(num)

print("A lista de números inteiros")
print(lista)
print("O número maior: ", max(lista))
print("O número menor:", min(lista))
