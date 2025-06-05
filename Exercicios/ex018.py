#AULA 08

#FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E
#MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE.

import math

angulo = float(input('Digite um angulo: '))
#ATENÇÃO POIS A DOCUMENTAÇÃO EXPLICA QUE DEVE SE PASSAR O VALOR EM RADIANOS
#POR ISSO É NECESSARIO CONVERTER O VALOR EM GRAUS ANTES DE EXIBIR
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O angulo de {angulo}º, possui: \nSeno de: {seno:.2f} '
      f'\nCosseno de: {cosseno:.2f} \nTangente de: {tangente:.2f}')