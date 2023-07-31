'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:'''
import datetime

# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alista
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

amarelo = '\033[0;30;43m'
verde = '\033[0;30;42m'
vermelho = '\033[0;31m'
limpar = '\033[0m'

anoNascimento = float(input('Favor informe o ano de seu nascimento?'))
anoAtual = datetime.datetime.now().year
diferenca = anoAtual - anoNascimento

if  diferenca < 18:
    print('{}Você ainda vai se alistar ao serviço militar{}'.format(verde,limpar))
    print('{}Ainda faltam {} anos para você poder se alistar{}'.format(verde,18 - diferenca,limpar))
elif    diferenca == 18:
    print('{}Está na hora de se alistar{}'.format(amarelo,limpar))
else:
    print('{}Já passou do tempo do alistamento{}'.format(vermelho, limpar))
    print('{}Já se passaram {} anos do prazo de seu alistamento{}'.format(vermelho,diferenca - 18,limpar))





