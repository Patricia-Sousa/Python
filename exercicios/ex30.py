# Estamos a gerir um bar e temos duas listas de clientes:
# A black_list: uma lista com clientes que, de alguma forma o seu comportamento é sancionável.
# Esta lista é composta inicialmente pelos seguintes nomes: André, Joana, Josefina, Filipa e Pedro
# A lista de clientes a lista de clientes para uma determinada festa que deve ser solicitada ao relações públicas
# O programa deverá perguntar se pretendem adicionar, em primeiro lugar, clientes à lista negra.
# Em caso afirmativo, deverá ser, em primeiro lugar, apresentada a lista atual e só depois pedir os nomes seguintes
# (sugere-se a comparação entre listas)
# Solicitar a lista de convidados
# Verificar se a lista de convidados contém os nomes da lista negra e retirá-los
# Apresentar a lista de convidados final

lista_negra = ['André', 'Joana', 'Josefina', 'Filipa', 'Pedro']
lista_convidados = []
print("Pretende adicionar clientes à lista negra [s] [n]")
while True:
    opcao = str(input())
    if opcao in ('s', 'n'):
        break

if opcao == 's':
    print("Lista de atual")
    print(lista_negra)
    print("Adicionar à lista")
    nome = str(input())
    if lista_negra.count(nome) == 0:
        lista_negra.append(nome)
elif opcao == 'n':
    print("O relações-públicas deve introduzir a lista de convidados")
    print("Número total de elementos da lista?")
    numero = int(input())
    print(":")
    for i in range(numero):
        convidado = str(input())
        lista_convidados.append(convidado)

    print("Lista de convidados")
    print(lista_convidados)
else:
    print("Fim do programa.")

print("Lista negra atualizada")
print(lista_negra)

for palavra_n in lista_negra:
    for palavra_c in lista_convidados:
        if palavra_n == palavra_c:
            lista_convidados.remove(palavra_c)

print("Lista de convidados atualizada")
print(lista_convidados)
