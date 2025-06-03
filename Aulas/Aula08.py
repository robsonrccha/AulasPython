#Trabalhando com MÓDULOS
#https://www.python.org/

import math #OPERAÇÕES MATEMATICAS
import random #ALEATORIEDADE
num = 5

arredondamento = math.ceil(num) #ARREDONDA PRA CIMA
print(arredondamento)

arredondamento2 = math.floor(num) #ARREDONDA PRA BAIXO
print(arredondamento2)


print(f'{random.random():.2f}') #RANDON.RANDON INTERVALO FLOAT DE 0 A 1
print(random.randint(1,10)) #RANDON.RANDINT INTERVALO INTEIRO E VOCE ESCOLHE OS VALORES

