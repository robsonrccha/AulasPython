#AULA 07

#ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE Km PERCORRIDOS POR UM CARRO ALUGADO
#E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR, SABENDO
#QUE O CARRO CUSTA R$60 POR DIA E R$0.15 POR Km RODADO

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

valor = (dias * 60) + (km * 0.15)

print(f'O valor a pagar pelo aluguel do carro é: {valor:.2f}')