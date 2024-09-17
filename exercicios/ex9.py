# Escreva um programa, que dada uma lista de números inteiros pelo utilizador,
# verifique se esta está ordenada por ordem crescente.
# Mostre no ecrã a lista ordenada.

lista_numeros = []

print("Introduza uma lista de números inteiros: [MAX 5 números]")

for i in range(5):
    numero = input()
    numero = int(numero)
    lista_numeros.append(numero)

print("Lista introduzida")
print(lista_numeros)

lista_numeros.sort()

print("Lista ordenada por ordem crescente")
print(lista_numeros)
