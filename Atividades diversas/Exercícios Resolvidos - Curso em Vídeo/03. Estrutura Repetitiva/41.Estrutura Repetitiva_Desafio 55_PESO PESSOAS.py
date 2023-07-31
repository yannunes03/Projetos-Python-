'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''


peso = 0
n = 1

peso = int(input(f'Favor informe o peso da {1}ª pessoa?'))
maiorPeso = peso
menorPeso = peso


for cont in range(0,4):
    n+= 1
    peso = int(input(f'Favor informe o peso da {n}ª pessoa?'))
    if peso >= maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso


print(f'O maior peso informado foi de {maiorPeso} Kg, e o menor peso foi {menorPeso} Kg')