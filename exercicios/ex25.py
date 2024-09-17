# Peça ao utilizador para selecionar uma figura geométrica: quadrado, retângulo
# e círculo. Calcule a área e o perímetro da figura selecionada.

print("Selecione uma figura geométrica: \nQuadrado - Q \nRetângulo - R \nCírculo - C \n-->")
escolha = str(input())
if (escolha == 'Q') or (escolha == 'q'):
    print("Cálculo da área e do perímetro de um quadrado")
    print("Introduza o lado:")
    lado = float(input())
    print("ÁREA: ", lado * lado)
    print("PERÍMETRO: ", lado * 4)
elif (escolha == 'R') or (escolha == 'r'):
    print("Cálculo da área e do perímetro de um retângulo")
    print("Introduza o comprimento:")
    comprimento = float(input())
    print("Introduza a altura:")
    altura = float(input())
    print("ÁREA: ", comprimento * altura)
    print("PERÍMETRO: ", (comprimento * 2 + altura * 2))
elif (escolha == 'C') or (escolha == 'c'):
    print("Cálculo da área e do perímetro de um círculo")
    print("Introduza o raio:")
    raio = float(input())
    print("ÁREA: ", (3.14159 * raio ** 2))
    print("PERÍMETRO: ", (2 * 3.14159 * raio))
else:
    print("Introduziu uma opção que não está disponível")