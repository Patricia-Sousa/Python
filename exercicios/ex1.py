# Peça um número inteiro e apresente o seu antecessor e o sucessor.

print('Introduza um número inteiro: ')
numero=int(input())
antecessor=int(numero-1)
sucessor=int(numero+1)
print('Antecessor: ' + str(antecessor)) #+ para str e , para int/float (concatenação)
print('Sucessor: ' + str(sucessor))
print(' ')

