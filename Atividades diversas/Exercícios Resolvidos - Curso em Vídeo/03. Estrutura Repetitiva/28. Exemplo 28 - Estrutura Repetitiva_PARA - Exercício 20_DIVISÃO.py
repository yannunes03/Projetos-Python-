'''
Escreva um algoritmo que leia um número inteiro N, e depois repita N vezes: ler dois números e imprimir
o resultado da divisão do primeiro pelo segundo. Caso não for possível, mostre a mensagem "DIVISAO
IMPOSSÍVEL"
'''

N: int ; i: int ; numerador: int ; denominador:int

N = int(input('Quantos casos você vai digitar? '))

for i in range(0, N):
    numerador = (int(input('Entre com o numerador: ')))
    denominador = (int(input('Entre com o denominador: ')))

    if denominador == 0:
        print('DIVISÃO IMPOSSÍVEL')
    else:
        print('Divisão = ', numerador / denominador)
