'''
Fazer um programa para ler dois números inteiros, e dizer se um número é múltiplo do outro. Os números podem ser digitados
em qualquer ordem.
'''

x: int ; y: int

print('Digite dois números inteiros: ')
x = int(input('1º Número: '))
y = int(input('2º Número: '))

if x % y == 0:
    print('Múltiplos')
else:
    print('Números não múltiplos')
