'''
Fazer um programa para ler um número natural N (valor máximo: 15), e depois calcular e mostrar o
fatorial de N
'''

N: int ; NFatorial: int ; NFatorial: int

N = int(input('Digite o valor de N: '))
NFatorial = N
Fatorial = 1

for i in range(0, N-1):
    NFatorial = NFatorial - 1
    Fatorial = Fatorial * NFatorial

print('FATORIAL = ', N * Fatorial)