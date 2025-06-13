#AULA07 - Operadores Aritméticos

#ADIÇÃO +
#SUBTRAÇÃO -
#MULTIPLICAÇÃO *
#DIVISAO /
#POTENCIA **
#DIVISAO INTEIRA //
#MODULO(RESTO DA DIVISÃO) %

soma = 5 + 2 # 7
subtrair = 5 - 2 # 3
multiplicar = 5 * 2
dividir = 5 / 2 # 10
potencia = 5 ** 2 # 25
divisorInteiro = 5 // 2 # 2
modulo = 5 % 2 # 1

#ORDEM DE PRECEDENCIA
# 1. ()
# 2. **
# 3. * / // %
# 4. + -

exemplo1 = 5 + 3 * 2 # 11
print(exemplo1)

exemplo2 = 3 * 5 + 4 ** 2 # 31
print(exemplo2)

exemplo3 = 3 * (5 + 4) ** 2 # 243
print(exemplo3)

potencia2 = pow(4, 3) #FUNCAO PARA POTENCIA, MAS AO USAR PERDE A ORDEM DE PRECEDENCIA
print(potencia2)

#PARA REALIZAR RAIZ QUADRADA É O MESMO QUE CRIAR A POTENCIA POR MEIO
raiz2 = 81**(1/2)
print(raiz2)

#RAIZ CUBICA
raiz3 = 127 ** (1/3)
print(raiz3)

#FORMATAÇÃO COM ALINHAMENTO < ^ > E PREENCHIMENTO * = - ETC
nome = input('Digite seu nome: ')
print(f'Olá {nome:*^20}, prazer em te conhecer', end = ' :)')
