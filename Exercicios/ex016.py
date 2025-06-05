#AULA 08

#CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL PELO TECLADO
#E MOSTRE NA TELA A SUA PORÇÃO INTEIRA

import math

num = float(input('Digite um valor do tipo float: '))

print(f'O numero {num} tem a parte inteira {math.trunc(num)}')

#OUTRA FUNCAO INTERNA É USAR O INT
print(f'O numero {num} tem a parte inteira {int(num)}')

#OUTRA OPCAO É USAR A ESCOLHA DE CASAS DECIMAIS
print(f'O numero {num} tem a parte inteira {num:.0f}')