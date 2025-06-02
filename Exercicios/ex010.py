#AULA 07

#CRIE UM PROGRAMA QUE LEIA QUANTO DINEHIRO UMA PESSOA TEM NA CARTEIRA
#E MOSTRE QUANTOS DOLARES ELA PODE COMPRAR
#CONSIDERE US$1.00 = R$3.27

reais = float(input('Quanto dinheiro você tem na carteira: R$'))
dolar = reais / 3.27
euro = reais / 6.50

print(f'Você tem R${reais:.2f} e com esse valor pode comprar US${dolar:.2f}')
print(f'Em euro voce pode comprar ${euro:.2f} euros')