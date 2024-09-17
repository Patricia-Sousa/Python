# Calcular a área do Círculo Pi*R^2
# importar o módulo math (para aplicar conceitos matemáticos)
import math
# Imprimir no ecrã uma mensagem
print('ÁREA DO CÍRCULO')
print('Raio: ')
# Criação de uma variável para guardar o valor introduzido pelo utilizador, com o tipo
# de dados float
raio = float(input())
# Criação de variável para guardar o resultado de uma fórmula matemática,
# math.pi * (raio ** 2)
# math.pi utiliza o valor do número pi guardado no módulo math
# print(math.pi)
# ** calcula a potência de um número
area = math.pi * (raio ** 2)
# Imprime no ecrã texto + o resultado que ficou guardado na variável area
print('Área: ', area)

