# Fatorial de um Número
# Escreva um programa que peça ao utilizador um número e calcule o fatorial desse número.

import math
print("Calculo do fatorial de um Número")
print("Insira um número inteiro:")
num = int(input())
#Se for introduzido um número inteiro negativo
if num < 0:
    numInt = int(math.fabs(num))
    print("Fatorial do número: ", numInt, " = ", math.factorial(numInt))
else:
    print("Fatorial do número: ", num, " = ", math.factorial(num))