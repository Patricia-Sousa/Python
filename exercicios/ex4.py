# Peça 2 números inteiros diferentes e diga qual é o maior

print('Número 1: ')
num1 = int(input())
print('Número 2: ')
num2 = int(input())
if num1 == num2:
    print('Os números são iguais.')
elif num1 > num2:
    print('O número', num1, 'é maior que o número 2.')
else:
    print('O número', num2, 'é maior que o número 1.')