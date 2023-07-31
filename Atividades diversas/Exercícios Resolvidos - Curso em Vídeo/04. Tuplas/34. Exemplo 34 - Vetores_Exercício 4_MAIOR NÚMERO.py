N: int ; par: int

N = int(input('Quantos números você vai digitar? '))
vetor: [float] = [0 for x in range(N)]

for c in range(0,N):
    vetor[c] = float(input('Digite um número para a posição {}: '.format(c)))
print()
print('NÚMEROS PARES: ')
print()

par = 0
for c in range(0,N):
    if vetor[c] % 2 == 0:
        print(vetor[c])
        par = par + 1
print()
print('QUANTIDADE DE PARES = ')
print(par)