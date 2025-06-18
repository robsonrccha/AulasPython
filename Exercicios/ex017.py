#AULA 08

#FACA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO
#E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO, CALCULE E
#MOSTRE O COMPRIMENTO DA HIPOTENUSA

import math

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)

print(f'A hipotenusa dos catetos é: {hipotenusa:.2f}')


#MATEMATICAMENTE: a hipotenusa é a raiz quadrada da soma dos quadrados do cateto
oposto2 = float(input('Digite o valor do cateto oposto: '))
adjacente2 = float(input('Digite o valor do cateto adjacente: '))
hipotenusa2 = (oposto2 ** 2 + adjacente2 ** 2) ** (1/2)

print(f'A hipotenusa2 dos catetos é: {hipotenusa2:.2f}')
