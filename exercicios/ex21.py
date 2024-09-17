# Uma empresa de informática está a proceder ao recrutamento de programadores em Python.
# Para isso serão realizadas entrevistas.
# Antes das entrevistas foram já selecionados alguns candidatos. Faça um programa que:
# Receba a lista inicial de candidatos, através do seu nome próprio e apelido
# Permita eliminar candidatos que não tenham comparecido à entrevista
# Permita acrescentar candidatos que, por lapso, ou indicação superior não foram inseridos
# No final, deverá apresentar a lista inicial e a lista final dos candidatos.
# A primeiro por ordem crescente. A seguida por ordem inversa.

lista_inicial_cand = []
print("Lista inicial de candidatos")
print("TOTAL de candicatos")
total_cand_iniciais = int(input())
for i in range(total_cand_iniciais):
        print("Nome e Apelido:")
        nome_com = str(input())
        nome_com = nome_com.lower()
        lista_inicial_cand.append(nome_com)

print("Lista inicial")
print(lista_inicial_cand)
print()
print("Eliminar candidatos [a]   Inserir candidatos [i]    Sair [0]")
escolha = str(input())
escolha = escolha.lower()
if escolha == 'a':
    print("Eliminar candidatos")
    print("Introduza o nome e apelido do candidato")
    elim_cand = str(input())
    elim_cand = elim_cand.lower()
    for i in lista_inicial_cand:
        if i == elim_cand:
            lista_inicial_cand.remove(i)
elif escolha == 'i':
    print("Inserir candidatos")
    print("Introduza o nome e apelido do candidato")
    ins_cand = str(input())
    ins_cand = ins_cand.lower()
    lista_inicial_cand.append(ins_cand)
elif escolha == '0':
    print("Fim do programa.")
else:
    print("Erro")

print("Lista Final de Candidatos")
print(lista_inicial_cand)
print("Lista ordenada alfabeticamente")
lista_inicial_cand.sort()
print(lista_inicial_cand)
print("Lista ordenada de forma inversa")
lista_inicial_cand.reverse()
print(lista_inicial_cand)
print("Fim do programa")