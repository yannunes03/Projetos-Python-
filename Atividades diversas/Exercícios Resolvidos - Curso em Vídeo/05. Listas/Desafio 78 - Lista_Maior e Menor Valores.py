'''Faça um programq que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista'''

lista = []
posicoesMaior = ''
posicoesMenor = ''
nMaior = 0
nMenor = 0



for ordem in range(0,5):
    lista.append(int(input(f'Informe um número para ocupar a {ordem + 1}ª posição da lista: ')))

maiorValor = max(lista)
menorValor = min(lista)

for ordem in range(0, len(lista)):
    if maiorValor == lista[ordem]:
        posicoesMaior = posicoesMaior + str(f'{ordem}...')
        nMaior+= 1
if nMaior > 1:
    strMaior = str(f' e suas posições na lista são {posicoesMaior} ')
else:
    strMaior = str(f' e sua posição na lista é {posicoesMaior}')

ordem = 0
for ordem in range(0, len(lista)):
    if menorValor == lista[ordem]:
        posicoesMenor = posicoesMenor + str(f'{ordem}...')
        nMenor+= 1

if nMenor > 1:
    strMenor = str(f'e suas posições na lista são {posicoesMenor}')
else:
    strMenor = str(f'e sua posição na lista é {posicoesMenor}')

print(f'A lista completa é: {lista}')
print(f'O maior valor informado foi o número {maiorValor} {strMaior}')
print(f'O Menor valor informado foi o número {menorValor} {strMenor}')


