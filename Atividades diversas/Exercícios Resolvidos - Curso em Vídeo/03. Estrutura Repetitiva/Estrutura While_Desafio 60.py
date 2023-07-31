'''Faça um programa que leia um número qualquer e mostre seu fatorial'''

n = int(input('Informe um número para que possamos lhe informar o seu fatorial: '))
fatorial = n

sequencia = ''

for cont in range(n,0,-1):
    if cont == 1:
        break
    fatorial = fatorial * (cont - 1)

for cont in range(n,0,-1):
    if cont == 1:
        break
    sequencia = sequencia + str(f'{cont}X')

print(f'{n}! = {sequencia}1 = {fatorial}')