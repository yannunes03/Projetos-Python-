'''
Fazer um programa para ler três números inteiros. EM seguida, mostrar qual o menor dentre os três
números lidos. EM caso de empate, mostrar apenas uma vez.
'''

x: int ; y: int ; z: int

x = input('Digite o primeiro valor: ')
y = input('Digite o segundo valor: ')
z = input('Digite o terceiro valor: ')

#Escrituração de Dados | Placeholder | Forma atual, moderna e tendência
if int(x) < int(y) and int(x) < int(z):
    print('MENOR = {}'.format(x))
elif int(y) < int(x) and int(y) < int(z):
    print('MENOR = {}'.format(y))
else:
    print('MENOR = {}'.format(z))

#Escrituração de Dados | Placeholder | Forma atual, moderna e tendência
if int(x) < int(y) and int(x) < int(z):
    print(f'MENOR = {x}')
elif int(y) < int(x) and int(y) < int(z):
    print(f'MENOR = {y}')
else:
    print(f'MENOR = {z}')

#Escrituração de Dados | Apenas Escriturando | Forma mais antiga, simples, porém em desuso
if int(x) < int(y) and int(x) < int(z):
    print('MENOR = ', x)
elif int(y) < int(x) and int(y) < int(z):
    print('MENOR = ', y)
else:
    print('MENOR = ', z)
