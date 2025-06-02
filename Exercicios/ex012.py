#AULA 07

#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO
#E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTO

produto = float(input('Qual o valor do produto: R$'))
desconto = produto - (produto * 5/100)

print(f'Seu produto custava R${produto:.2f} e teve 5% de desconto na liquidação, \no valor dele agora é R${desconto:.2f}')