# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = float(input('Informe um número por favor, que iremos verificar se ele é PAR ou IMPAR'))

if num % 2 == 0:
    print(f'O numero informado, {num:.0F}, é PAR')
else:
    print(f'O número informado, {num:.0F}, é IMPAR')