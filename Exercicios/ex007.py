#AULA 07

#DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO, CALCULE E MOSTRE SUA MÉDIA
aluno = input('Qual o nome do aluno? ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

print(f'A média do aluno {aluno} é {media}')