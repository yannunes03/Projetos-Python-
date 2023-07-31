'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma Tupla.
No final mostre:'''

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares.

nPares = ''
contPares = 0
posicaoPares = ''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite o último númeor: '))

tupla = (n1, n2, n3, n4)
print(f'A dupla montada é {tupla}')

# Quantidade de vezes que o valor 9 apareceu:
if tupla.count(9) == 0:
    print('O Valor 9 não foi digitado nenhuma vez na tupla.')
else:
    print(f'A quantidade de vezes que o valor 9 apareceu foi de {tupla.count(9)} vezes')

# A posição que foi digitado o primeiro valor 3.
if tupla.count(3) == 0:
    print('O valor 3 não foi digitado nenhuma vez na tupla.')
else:
    print(f'O primeiro valor 3 digitado está na posição {tupla.index(3)} dupla')

# Quais foram os números pares.
for cont in tupla:
    if cont >= 4:
        break
    if tupla[cont] % 2 == 0:
        nPares = nPares + str(f'{tupla[cont]}... ')
        posicaoPares = posicaoPares + str(f'{cont}...')
        contPares+= 1

if contPares == 0:
    print('Não houveram números pares digitados e inputados na tupla')
else:
    print(f'Os números pares digitados foram {nPares}, nas seguintes e respectivas posições {posicaoPares}')





