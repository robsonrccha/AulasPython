#AULA 06

#FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE
#NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSIVEIS SOBRE ELA

valor = input('Digite algo: ')
print('O tipo primitivo do que foi digitado é:' ,type(valor),'\n')

print('É numerico?:' ,valor.isnumeric())
print('É alfabetico?:' ,valor.isalpha())
print('É alfanumerico?:' ,valor.isalnum())
print('Esta tudo em maiusculas?:' ,valor.isupper())
print('Esta tudo em minusculas?:' ,valor.islower())
print('Possuem as primeiras letras maiusculas de cada palavra?:' ,valor.istitle())
print('O conteúdo esta em branco?:' ,valor.isspace())
print('O conteúdo é todo digitos?:' ,valor.isdigit())
print('Pode ser usado como identificador(variavel)?:' ,valor.isidentifier())
print('O conteúdo pode ser exibido de forma visivel?:' ,valor.isprintable()) #False ex: 'Ola\nJosé' há quebra de linha, que não é exibido
print('O valor faz parte da tabela ASCII?:' ,valor.isascii()) #Emoji é False o "á" ou "ã", so retorna True se estiver entre A-Z, a-z, 0-9, !-@-#-... e \n-\t etc
