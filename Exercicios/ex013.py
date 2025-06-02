#AULA 07

#FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONARIO
#E MOSTRE SEU NOVO SALARIO COM 15% DE AUMENTO

salario = float(input('Digite seu salario: '))
aumento = salario + (salario * 15/100)

print(f'Parabens! Seu salario teve um aumento de 15%. Seu novo salario é: {aumento:.2f}')