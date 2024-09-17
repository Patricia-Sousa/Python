# Faça um programa para colocar os artigos diários em armazém.
# A informação a introduzir será o Nome do produto. Mostre a lista inserida pelo utilizador e
# apresente-a também por ordem alfabética.

print("LISTA: Artigos diários em armazém")
lista_artigos = []
print("Introduza [8 artigos]")
for i in range(8):
    artigo = str(input())
    artigo = artigo.lower()
    lista_artigos.append(artigo)
print("Lista introduzida")
print(lista_artigos)
lista_artigos.sort()
print("Lista ordenada alfabeticamente")
print(lista_artigos)
