'''Crie um programa que vai ler vários números e colocar uma lista'''

# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
#digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
lPares = list()
lImpares = list()
continuar = ''

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        lPares.append(n)
    else:
        lImpares.append(n)
    continuar = input('Deseja continuar [S/N]: ')
    if continuar == 'N' or continuar == 'n':
        break
print(f'A lista completa é {lista}')
print(f'A lista completa apenas com números pares fica da seguinte forma = {lPares}')
print(f'A lista completa apenas com números ímpares fica da seguinte forma = {lImpares}')

