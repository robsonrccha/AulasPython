#AULA 08

#ESCREVA UM PROGRAMA QUE LEIA O VALOR EM METROS
#E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS

metros = int(input('Digite um valor em metros: '))

centimetros = metros * 100
milimetros = metros * 1000

print(f'Você escolheu {metros}m, isso dá {centimetros}cm e {milimetros}mm.')