# Escreva um programa que peça um número indeterminado de valores, correspondentes a notas.
# A introdução dos valores deverá ser concluída quando for enviado o -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:
# Apresente a quantidade de valores que foram introduzidos;
# Apresente todos os valores na ordem em que foram introduzidos, uns debaixo dos outros;
# Calcule e apresente a soma dos valores;
# Calcule e apresente a média dos valores;
# Calcule e apresente a quantidade de valores acima da média calculada;
# Calcule e apresente a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem à sua escolha.

print("Introduza uma lista de valores [notas]      Sair [-1]")
numero = float(input())
lista = []
lista.append(numero)
while numero != -1:
    num = float(input())
    if num == -1:
        break
    lista.append(num)
else:
    print("Fim do programa.")

print("A lista introduzida")
print(lista)
comprimento_lista = len(lista)
soma_total_lista = sum(lista)
media_lista = float(soma_total_lista / comprimento_lista)
print("Dados após as entradas:")
print("Quantidade de valores:", comprimento_lista)
print("SOMA:", soma_total_lista)
print("MÉDIA:", media_lista)

# Calcule e apresente a quantidade de valores acima da média calculada;
lista_media = []
for elemento_m in lista:
    if elemento_m > media_lista:
        lista_media.append(elemento_m)

print("Lista de valores acima da média calculada")
print(lista_media)
print("Quantidade")
print(len(lista_media))

# Calcule e apresente a quantidade de valores abaixo de sete;
lista_auxiliar = []
for elemento_a in lista:
    if elemento_a < 7:
        lista_auxiliar.append(elemento_a)

print("Lista de valores abaixo de 7")
print(lista_auxiliar)
print("Quantidade")
print(len(lista_auxiliar))

print("Fim do programa.")


