'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

# Um número primo é aqui que é dividido apenas por um e por ele mesmo.

contador = 0

verificador = int(input('Favor informe um número que iremos verificar se ele é um número primo'))

for divisor in range(1,10):
    if  verificador % divisor == 0:
        contador += 1
    if verificador == divisor:
        contador -= 1
    if divisor == 1:
        contador -= 1

if contador != 0:
    print(f'O número {verificador} não é um número primo!')
else:
    print(f'O número {verificador} é um número primo!')


