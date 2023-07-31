'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles
que forem pares. Se o valor digitado for impar, desconsidere-o'''

soma = 0

for posicao in range(1,7):
    numeroDigitado = int(input(f'Informe um número para ocupar a posição {posicao}'))
    if  numeroDigitado % 2 ==0:
        soma = soma + numeroDigitado
print('A soma de todos os 6 números digitados e que eram pares é {}'.format(soma))




