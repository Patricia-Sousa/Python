# Escreva um programa que peça uma frase ao utilizador e devolva quantas vogais essa frase possui
# [a, e, i, o, u]

print('Introduza uma frase: ')
frase = str(input())
frase = frase.lower()
frase = list(frase)

lista_vogais = ['a', 'e', 'i', 'o', 'u']
#Lista para armazenar a quantidade de vogais
contagem_vogais = [0, 0, 0, 0, 0]

for letra in frase:
    for vogal in lista_vogais:
        if letra == vogal:
            posicao = lista_vogais.index(vogal)
            contagem_vogais[posicao] += 1

print("Ocorrências de vogais")
for i in range(len(lista_vogais)):
    print('[', lista_vogais[i], '], ocorre ', contagem_vogais[i])
