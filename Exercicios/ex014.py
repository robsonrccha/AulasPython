#AULA 07

#ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA
#DIGITADA EM ºC E CONVERTA PARA ºF
temperatura = float(input('Digite a temperatura em ºC: '))
formula = ((temperatura * 9) / 5) + 32 #FORMULA PARA DESCOBRIR ºF

print(f'A temperatura {temperatura}ºC corresponde a {formula}ºF')