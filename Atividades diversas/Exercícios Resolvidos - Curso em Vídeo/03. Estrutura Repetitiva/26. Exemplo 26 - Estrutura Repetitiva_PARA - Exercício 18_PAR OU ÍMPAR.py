'''
Leia um valor inteiro N. Este valor será a quantidade de números inteiros que serão lidos em seguida.
Para cada valor lido, mostre uma mensagem dizendo se este valor lido é PAR ou IMPAR, e também se é
POSITIVO ou NEGATIVO. No caso do valor ser igual a zero (o), seu programa deverá imprimir apenas NULO
'''


N: int ; i: int ; x: int
ParOuImpar: str ; PositivoOuNegativo: str

N = int(input('Quantos numeros voce vai digitar? '))

for i in  range(0, N):
    x = int(input('Digite um número? '))
    if x == 0:
        ParOuImpar = 'NULO'
    elif x % 2 == 0:
        ParOuImpar = 'PAR'
    else:
        ParOuImpar = 'IMPAR'
    if x == 0:
        PositivoOuNegativo = ''
    elif x > 0:
        PositivoOuNegativo = 'POSITIVO'
    else:
        PositivoOuNegativo = 'NEGATIVO'
    print('{} e {}'.format(ParOuImpar, PositivoOuNegativo))

