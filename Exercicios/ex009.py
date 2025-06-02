#AULA 07

#FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO QUALQUER
#E MOSTRE NA TELA A SUA TABUADA

num = int(input('Escolha um numero: '))
contador = 1
print('\t')

print(f'O numero escolhido foi o "{num}", a tabuada dele é:')

while contador <= 10:
    print(f'{num} x {contador} = {num * contador}')
    contador += 1
