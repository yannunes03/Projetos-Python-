'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressão usando a estrutura While.
'''

termo1 = int(input('Defina o 1º termo da progressão aritmética'))
razao = int(input('Qual será a razão desta progressão aritmética?'))

soma = termo1
print(soma)
sequencia = str(f'{soma}')

cont = 1

while cont < 10:
    soma = soma + razao
    sequencia = sequencia +  ',' + str(f'{soma}')
    cont+= 1
print('A sequência da progressão aritmética ficará da seguinte forma = {' + sequencia + '}')