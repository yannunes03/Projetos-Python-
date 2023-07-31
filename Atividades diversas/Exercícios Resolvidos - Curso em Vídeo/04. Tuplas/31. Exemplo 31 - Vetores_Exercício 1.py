c: int ; N: int ; Contagem: int
Contagem = 1

N = int(input('Quantos Números você vai digita? '))

vet: [float] = [0 for x in range(N)]

for c in range(0,N):
    vet[c] = float(input('Digite um número: '))

print()
print('Números Negativos: ')

for c in range(0,N):
    if vet[c] < 0:
        print('Número Negativo {}: {}'.format(Contagem,vet[c]))
        Contagem = Contagem + 1

