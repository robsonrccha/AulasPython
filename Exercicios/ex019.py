#AULA 08

#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO.
#FACA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DELES E ESCREVENDO O NOME DO ESCOLHIDO

import random

alunos = []
contador = 1

while True:
    alunos.append(input(f'Qual nome do(a) {contador}º aluno(a): '))
    if contador == 4:
        break
    contador += 1

print('\t')

escolhido = random.choice(alunos)
print(f'O aluno(a) escolhido foi o(a): {escolhido}')
