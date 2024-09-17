# Encontrar o elemento mais frequente:

lista = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 8, 9]

def elemento_mais_frequente(lista):
    elemento_mais = []
    frequencia_max = 0

    for elemento in lista:
        frequencia = lista.count(elemento)
        if frequencia > frequencia_max:
            frequencia_max = frequencia
            elemento_mais = elemento

    return elemento_mais

print(lista)
print(elemento_mais_frequente(lista))