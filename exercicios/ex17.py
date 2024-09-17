# No início de uma sessão de formação, é feita a chamada dos formandos presentes e são colo
# numa lista pelo formador. A lista completa deverá ser mostrada.
# Durante a sessão poderão ser acrescentados ou eliminados nomes de acordo com as presenças
# No final deverá apresentar: Os formandos que integraram inicialmente; o conjunto de forma
# com as entradas após hora de chamada; o conjunto de formandos que saíram após a hora da c
# Todas as listas devem ser apresentadas por ordem alfabética.

def principal():
    lista_inicial = []
    lista_entradas = []
    lista_saidas = []
    lista_e = []
    lista_s = []

    print("Lista de formandos: [Introduza o número total de formandos]")
    num_total = int(input())

    for i in range(num_total):
        print("Introduza o nome:")
        nome = str(input())
        nome = nome.lower()
        lista_inicial.append(nome)

    print("Lista completa inicial")
    print(lista_inicial)

    print("Gestão da lista para entradas ou saídas depois da hora de chamada")
    print("Entradas [e] Saídas [s]           Sair [0]")
    escolha = str(input())
    escolha = escolha.lower()
    while (escolha == 'e') or (escolha == 's') or (escolha == '0'):
        if escolha == 'e':
            lista_entradas = lista_inicial
            print("Nome do formando:")
            nome_e = str(input())
            nome_e = nome_e.lower()
            if nome_e not in lista_inicial:
                lista_entradas.append(nome_e)
            print("Sair [0] Continuar [e] [s]")
            escolha = str(input())
            escolha = escolha.lower()
        elif escolha == 's':
            print("Nome do formando:")
            lista_saidas = lista_inicial
            nome_s = str(input())
            nome_s = nome_s.lower()
            if nome_s in lista_inicial:
                lista_saidas.remove(nome_s)
            print("Sair [0] Continuar [e] [s]")
            escolha = str(input())
            escolha = escolha.lower()
        elif escolha == '0':
            break
        else:
            print("Opção inválida.")
    else:
        print("Opção inválida.")

    print("Lista de entradas")
    for nome in lista_entradas:
        nome_cap = nome.capitalize()
        lista_e.append(nome_cap)
    print(lista_e)
    print("Lista de saídas")
    for nome in lista_saidas:
        nome_cap = nome.capitalize()
        lista_s.append(nome_cap)
    print(lista_s)


principal()