# Dadas 2 dimensões dos catetos de um triângulo retângulo
# determine a dimensão da hipotenusa.
# Teorema de pitágoras: h^2 = c^2 + c^2
# Hipotenusa: math.sqrt(cateto^2 + cateto^2)

import math
print("Cálculo da hipotenusa de um triângulo retângulo")
print("Introduza a medida do cateto 1:")
cateto1 = float(input())
print("Introduza a medida do cateto 2:")
cateto2 = float(input())
#math.sqrt(x) - raiz quadrada
hipotenusa = float(math.sqrt(cateto1 ** 2 + cateto2 ** 2))
print("Hipotenusa: ", hipotenusa)