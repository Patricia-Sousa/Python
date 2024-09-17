# Faça um programa em Python que receba uma lista de valores numéricos do utilizador.
# Crie um menu que permite que o utilizador selecione uma das seguintes operações:
# Soma dos valores da lista
# Duplicação dos valores da lista (deverá perguntar quantas vezes pretende duplicar)
# Ordenar a lista por ordem crescente
# Ordenar a lista por ordem inversa
# Eliminar um elemento através do seu valor
# (perguntar o valor que pretende eliminar.
# Ao selecionar esta opção deverá receber, em primeiro lugar, os elementos da lista)
# Eliminar um elemento através do seu índice
# (perguntar o índice do valor que pretende eliminar. Ao selecionar esta opção deverá receber, em primeiro lugar,
# uma mensagem com a quantidade de elementos da lista)

lista_inteiros = []
print("Insira o total de elementos da sua lista de números inteiros")
num = int(input())
print("Insira a sua lista")
for i in range(num):
    print("Índice: ", i)
    num_l = int(input())
    lista_inteiros.append(num_l)

print("MENU")
print("[1] Soma dos valores da lista")
print("[2] Duplicação dos valores da lista")
print("[3] Ordenar a lista por ordem crescente")
print("[4] Ordenar a lista por ordem inversa")
print("[5] Eliminar um elemento através do seu valor")
print("[6] Eliminar um elemento através do seu índice")
print()
print("0pção")
opcao = str(input())
if opcao == '1':
    print("[1] Soma dos valores da lista")
    print(sum(lista_inteiros))
elif opcao == '2':
    print("[2] Duplicação dos valores da lista")
    print("Quantas x quer duplicar?")
    x = int(input())
    print(lista_inteiros * x)
elif opcao == '3':
    print("[3] Ordenar a lista por ordem crescente")
    lista_inteiros.sort()
    print(lista_inteiros)
elif opcao == '4':
    print("[4] Ordenar a lista por ordem inversa")
    lista_inteiros.reverse()
    print(lista_inteiros)
elif opcao == '5':
    print("[5] Eliminar um elemento através do seu valor")
    print("ELementos da lista")
    print(lista_inteiros)
    print("Qual o valor que deve ser eliminado?")
    num_e = int(input())
    for elemento in lista_inteiros:
        if elemento == num_e:
            lista_inteiros.remove(elemento)
    print("Lista", lista_inteiros)
elif opcao == '6':
    print("[6] Eliminar um elemento através do seu índice")
    print("Comprimento da lista de inteiros")
    print(len(lista_inteiros))
    print("Qual o índice do valor que deve ser eliminado?")
    num_i = int(input())
    for i in range(len(lista_inteiros)):
        if i == num_i:
            lista_inteiros.pop(i)
    print("Lista", lista_inteiros)
else:
    print("Erro")
