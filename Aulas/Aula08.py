#AULA08 - Utilizando Módulos

#Documentação
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


#VALOR BASE PARA TESTES
x = 9
y = -3.7
z = 2.0

print(f'Raiz quadrada de {x}:', math.sqrt(x))  #RETORNA A RAIZ QUADRADA DE x
print(f'Valor absoluto de {y}:', math.fabs(y))  #RETORNA O VALOR ABSOLUTO (FLOAT)
print(f'Fatorial de {x}:', math.factorial(x))  #RETORNA O FATORIAL DE x (x DEVE SER INTEIRO >= 0)
print(f'{x} elevado à potência {z}:', math.pow(x, z))  #RETORNA x ELEVADO A z (POTENCIA)
print(f'Logaritmo natural de {x}:', math.log(x))  #LOGARITMO NATURAL (BASE E)
print(f'Logaritmo de {x} na base 10:', math.log10(x))  #LOGARITMO NA BASE 10
print(f'Logaritmo de {x} na base 2:', math.log2(x))  #LOGARITMO NA BASE 2
print(f'Arredondamento para baixo de {y}:', math.floor(y))  #ARREDONDA PARA BAIXO
print(f'Arredondamento para cima de {y}:', math.ceil(y))  #ARREDONDA PARA CIMA
print(f'Parte inteira de {y}:', math.trunc(y))  #TRUNCA (REMOVE PARTE DECIMAL)
print(f'Cosseno de {z}:', math.cos(z))  #RETORNA O COSSENO DE Z (EM RADIANOS)
print(f'Seno de {z}:', math.sin(z))  #RETORNA O SENO DE Z (EM RADIANOS)
print(f'Tangente de {z}:', math.tan(z))  #RETORNA A TANGENTE DE z (EM RADIANOS)
print(f'Convertendo graus para radianos (90):', math.radians(90))  #CONVERTE GRAUS PARA RADIANOS
print(f'Convertendo {x} radianos para graus (π):', math.degrees(x))  #CONVERTE RADIANOS PARA GRAUS
print(f'Máximo divisor comum de 12 e 18:', math.gcd(12, 18))  #RETORNA O MÁXIMO DIVISOR COMUM
print(f'Constante pi:', math.pi)  #VALOR DE π
print(f'Constante e:', math.e)  #VALOR DE E (BASE DO LOGARITMO NATURAL)
print(f'Hipotenusa de um triângulo com catetos 3 e 4:', math.hypot(3, 4))  # √(3² + 4²)
print(f'Exponencial de {z} (e^z):', math.exp(z))  #RETORNA E ELEVADO A z


