#AULA 09 - MANIPULANDO CADEIA DE TEXTOS

frase = 'Curso em Video Python' #CADA CARACTER É GUARDADO DENTRO DE UM INDICE, INCLUINDO OS ESPAÇOS

#FATIAMENTO
print(frase[9]) #BUSCA O INDICE 9
print(frase[9:21]) #BUSCA DO 9 AO 20(SEMPRE UM A MENOS QUE O NUMERO FINAL)
print(frase[9:21:2]) #BUSCA DO 9 AO 20 PULANDO DE 2 EM 2
print(frase[:5]) #BUSCA DO INDICE 0 ATÉ O 4(5 MENOS 1 ATÉ O 4)
print(frase[15:]) #BUSCA DO INDICE 15 ATÉ O FINAL DA STRING
print(frase[9::3]) #BUSCA DO 9 ATE O FINAL PULANDO DE 3 EM 3

print('\t')

#ANALISE
comprimento = len(frase) #COMPRIMENTO
print(comprimento)
contagem = frase.count('o') #CONTA QUANTOS "O" HÁ NA STRING
print(contagem)
contagem2 = frase.count('o', 0, 13) #CONTAGEM COM INICIO E FIM DA STRING PELO INDICE
print(contagem2)
busca = frase.find('deo') #BUSCA EXATAMENTE A PARTE SOLICITADA E MOSTRA O INICIO DO INDICE SE ENCONTRAR
print(busca)
busca2 = 'python' in frase.upper() #RETORNA BOLEANO SE SIM OU NÃO
print(busca2)

print('\t')

#TRANSFORMAÇÃO
print(frase.replace('Python', 'Java')) #SUBSTITUIÇÃO
print(frase.upper()) #TODOS OS CARACTERES EM MAIUSCULO
print(frase.lower()) #TODOS OS CARACTERES EM MINUSCULA
print(frase.capitalize()) #O PRIMEIRO CARACTER DA STRING EM MAIUSCULA
print(frase.title()) #A PRIMEIRA LETRA DE TODA PALAVRA EM MAIUSCULA

print('\t')

frase2 = '   Aprenda Python  '
print(frase2)
print(frase2.lstrip()) #REMOVE OS ESPAÇOS DA ESQUERDA
print(frase2.rstrip()) #REMOVE OS ESPAÇOS DA DIREITA
print(frase2.strip()) #REMOVE OS ESPAÇOS DO INICIO E FIM DA STRING

print('\t')

#DIVISAO
frase3 = 'Curso-em-Video-Python'
print(frase.split()) #POR PADRAO SEPARA PELOS ESPAÇOS, ONDE CADA PALAVRA NOVA RECEBA UMA NOVA INDEXAÇÃO E MOSTRA COMO LISTA
print(frase3.split('-')) #SEPARA PELO DELIMITADOR ESPECIFICADO
print(frase3.split('-', 2)) #SEPARA PELO DELIMITADOR E PELO NUMERO DE DIVISOES

print('\t')

#JUNÇÃO
frase4 = frase.split()
print(frase4)
print(' '.join(frase4)) #FAZ A JUNÇAO DA FRASE SEPARADA COM O DELIMITADOR ESTIPULADO