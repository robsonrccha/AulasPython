#AULA 08

#O MESMO PROFESSOR DO DESAFIO ANTERIOR QUER SORTEAR A ORDEM DE APRESENTAÇO
#DE TRABALHO DOS ALUNOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS
#E MOSTRE A ORDEM SORTEADA

import random

alunos = []
contador = 1

while True:
    alunos.append(input(f'Digite o nome do {contador}º aluno: '))
    if contador == 4:
        break
    contador += 1

random.shuffle(alunos)
print(f'A ordem de apresentação sera {alunos}')