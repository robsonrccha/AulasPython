#AULA 06

#TIPO INTEIRO INT
num1 = int(input('Digite um numero: '))

#TIPO FLUTUANTE
num2 = float(input('Escolha um valor: '))

#TIPO BOOLEANO
idade = int(input('Digite sua idade: '))
maiorIdade = 18
print(f'Vocé é maior de idade?: {maiorIdade <= idade}\n') #VALIDAÇAO BOOLEANA

#TIPO STRING
msg = 'Olá'

print('O tipo da variavel "num1" é:' ,type(num1))
print('O tipo da variavel "num2" é:',type(num2))
print('O tipo da variavel "msg" é:',type(msg),'\n')

#USO DO "is" PARA STRINGS: ALGUNS EXEMPLOS
print('O valor da variavel "msg" esta todo em letras maiusculas?:' ,msg.isupper()) #VERIFICA SE O TESTO ESTA EM MAIUSCULAS
print('O valor da variavel "msg" esta todo em letras minusculas?:' ,msg.islower()) #VERIFICA SE ESTA EM MINUSCULAS
print('O valor da variavel "msg" é numerico?:' ,msg.isnumeric()) #VERIFICA SE É NUMERICO
print('O valor da variavel "msg" esta em letras(alpha)?:' ,msg.isalpha()) #VERIFICA SE ESTA EM LETRAS ALFABETICAS(SE HOUVER ESPAÇOS OU VIRGULAS SERÁ False
print('O valor da variavel "msg" é alfanumerico?:' ,msg.isalnum(),'\n') #VERIFICA SE É ALFANUMERICO
