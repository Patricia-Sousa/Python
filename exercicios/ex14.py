# Os professores de Ed. Física estão a selecionar pessoas para montar uma equipa de natação.
# Para isso convocaram os 7 melhores tempos da última competição.
# Considerando que não houve tempos iguais construa um programa que leia o nome e o tempo (em segundos)
# de cada atleta e calcule o tempo médio dos nadadores.
# Nota: Crie duas listas, uma para colocar os nomes dos nadadores, e outra para guardar os tempos.

nadadores= ['João', 'André', 'Raquel', 'Patrícia', 'Isabel', 'Tiago', 'Miguel']
tempos = [46.1, 50.2, 60, 142.00, 342.00, 57.13, 151.92]

nadadores_total = len(nadadores)
tempo_total = sum(tempos)

for i in range(len(nadadores)):
    print("Nadador: ", nadadores[i])
    print("Tempo:", tempos[i])

print("O tempo médio dos nadadores é: ", float(tempo_total // nadadores_total))

