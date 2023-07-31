'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os
10 primeiros termos dessa progressão'''

'''Progressão aritmética é uma sequência numérica em que a diferença entre um termo e seu antecessor resulta
sempre em um mesmo valor, chamado de razão. Por exemplo, considere a sequência a seguir:'''
# (2,4,6,8,10,12,14,16,18,20...)
# Vamos observar o que acontece com a subtração de qualquer termo pelos seus antecessores:
'''
20 - 18 = 2
18 - 16 = 2
16 - 14 = 2
14 -12 = 2
'''


termo1 = int(input('Defina o 1º termo da progressão aritmética'))
razao = int(input('Qual será a razão desta progressão aritmética?'))

soma = termo1
print(soma)
sequencia = str(f'{soma}')

for quantidade in range(2,11):
    soma = soma + razao
    sequencia = sequencia +  ',' + str(f'{soma}')
print('A sequência da progressão aritmética ficará da seguinte forma = {' + sequencia + '}')