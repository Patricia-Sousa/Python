# Dado o preço de um produto e uma quantidade de dinheiro disponível,
# determine quantas unidades desse artigo pode comprar e
# quanto dinheiro sobra
# trunc int (vai buscar a parte inteira do número)
# // divisão inteira

import math
print('Preço do produto:')
precoProduto = float(input())
print('Insira o dinheiro para pagamento:')
dinheiro = float(input())
totalProdutos = int(dinheiro / precoProduto)
dinheiroFinal = int(dinheiro - (precoProduto * totalProdutos))
print('Total de produtos:', totalProdutos)
print('Dinheiro que sobra:', dinheiroFinal)