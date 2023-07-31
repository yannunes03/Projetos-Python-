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

