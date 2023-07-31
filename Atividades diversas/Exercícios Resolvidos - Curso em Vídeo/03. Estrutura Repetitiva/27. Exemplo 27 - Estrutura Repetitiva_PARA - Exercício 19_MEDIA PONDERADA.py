# O exercício consiste em, um número "N" vezes, realizar o cálculo de média ponderada, considerando 3 números.
N: int ; i: int
N1: float ; N2: float ; N3: float ; media: float

N = int(input('Quantos casos voce vai digitar? '))

for i in range(0,N):
    print('Digite tres numeros: ')
    N1 = float(input('Digite o 1º número: '))
    N2 = float(input('Digite o 2º número: '))
    N3 = float(input('Digite o 3º número: '))
    media = ((N1 * 2) + (N2 * 3) + (N3 * 5) / (2 + 3 + 5))
    print('MÉDIA = {:.2f}'.format(media))
