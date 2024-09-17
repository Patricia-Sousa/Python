# Escreva um programa que solicite uma frase ao utilizador, que pergunte qual a letra que pretende testar
# e que devolva o número de vezes que essa letra aparece na frase

print('Introduza uma frase: ')
frase = str(input())
frase = frase.lower()
frase = list(frase)

print('Escolha uma letra: ')
letra = input()
letra = letra.lower()

def qtd_letras(frase, letra):
    auxiliar = 0

    for elemento in frase:
        if elemento == letra:
            auxiliar += 1

    return auxiliar

qtd_let = qtd_letras(frase, letra)
print("Número de ocorrências de", letra, "na frase escrita: ", qtd_let)
