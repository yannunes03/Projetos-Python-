N: int ; i: int ; numerador: int ; denominador:int

N = int(input('Quantos casos você vai digitar? '))

for i in range(0, N):
    numerador = (int(input('Entre com o numerador: ')))
    denominador = (int(input('Entre com o denominador: ')))

    if denominador == 0:
        print('DIVISÃO IMPOSSÍVEL')
    else:
        print('Divisão = ', numerador / denominador)
