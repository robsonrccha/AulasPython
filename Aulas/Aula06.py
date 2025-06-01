#AULA 06

#TIPO INTEIRO INT
num1 = int(input('Digite um numero: '))

#TIPO FLUTUANTE
num2 = float(input('Escolha um valor: '))

#TIPO BOOLEANO
idade = int(input('Digite sua idade: '))
maiorIdade = 18
print(f'Vocé é maior de idade?: {maiorIdade <= idade}\n') #validaçao booleana

#TIPO STRING
msg = 'Olá'

print('O tipo da variavel "num1" é:' ,type(num1))
print('O tipo da variavel "num2" é:',type(num2))
print('O tipo da variavel "msg" é:',type(msg),'\n')

#USO DO "is" PARA STRINGS: alguns exemplos
print('O valor da variavel "msg" esta todo em letras maiusculas?:' ,msg.isupper()) #verifica se o testo esta todo em maiusculas
print('O valor da variavel "msg" esta todo em letras minusculas?:' ,msg.islower()) #verifica se esta todo em minuscula
print('O valor da variavel "msg" é numerico?:' ,msg.isnumeric()) #verifica se é numerico
print('O valor da variavel "msg" esta em letras(alpha)?:' ,msg.isalpha()) #verifica se esta em letras alfabeticas(se houver espaços ou virgulas será False
print('O valor da variavel "msg" é alfanumerico?:' ,msg.isalnum(),'\n') #verifica se é alfanumerico