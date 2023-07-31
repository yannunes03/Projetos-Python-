'''Faça um progrma que leia N números reais e armazene-os em um vetor. Em seguida:
- Imprimir todos os elementos do vetor
- Mostrar na tela a soma e a média dos elementos do vetor
'''

N: int ; Numero: int
soma: float ; media: float

Numero = 1
soma = 0

N = int(input('Quantos números você vai digitar? '))

meu_vetor: [float] = [0 for x in range (N)]

for c in range(0,N):
    meu_vetor[c] = float(input('Digite um número para o {}º espaço no vetor'.format(Numero)))
    Numero = Numero + 1

print('Valores = ')

for c in range(0,N):
    print(meu_vetor[c])
    soma = soma + meu_vetor[c]

media = soma / N

print()
print('Soma = {}'.format(soma))
print('Média = {}'.format(media))