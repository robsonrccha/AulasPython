#AULA 07

#CRIE UM ALGORITMO QUE LEIA UM NUMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA

num = int(input('Escolha um numero: '))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print(f'O numero escolhido foi "{num}", o dobro dele é: {dobro}, o triplo é: {triplo} e a raiz quadrada é: {raiz:.3f}')
