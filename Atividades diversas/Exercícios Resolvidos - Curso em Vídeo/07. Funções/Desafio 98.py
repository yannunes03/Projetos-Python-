'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
início, fim e passo e realize a contagem

Seu programa tem que realizar três contagens através da função criada:'''

# a) De 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) Uma contagem personalizada

import time

def contador(inicio, fim, passo):
    sequencia = ''
    for i in range(inicio, fim, passo):
        sequencia += str(f'{i}')
        time.sleep(1)
        print()

