#Crie um script que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem formatada
dia = int(input('Qual seu dia de nascimento?: '))
mes = input('Qual o mês?: ')
ano = int(input('Qual o ano de nascimento?: '))
anoAtual = 2025

print(f'Você nasceu em {dia} d0 {mes} de {ano}, você tem ou fará {anoAtual - ano}, parabens!')