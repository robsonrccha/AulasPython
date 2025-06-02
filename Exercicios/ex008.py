#AULA 08

#ESCREVA UM PROGRAMA QUE LEIA O VALOR EM METROS
#E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS

metros = float(input('Digite um valor em metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print(f'Você escolheu {metros}m, isso dá {centimetros:.0f}cm e {milimetros:.0f}mm.')
