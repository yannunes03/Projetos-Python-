'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular'''

tupla = ('Lápis', 'R$ 1.75',
         'Borracha', 'R$ 2.00',
         'Caderno', 'R$ 15.90',
         'Estojo', 'R$ 25.00',
         'Transferidor', 'R$ 4.20',
         'Compasso', 'R$ 9.99',
         'Mochila', 'R$ 120.32',
         'Canetas', 'R$ 22.30',
         'Livro', 'R$ 34.90',
         'Agenda', 'R$ 5.50',
         'Colher', 'R$ 10.25')
tr = '--'
tr2 = '.'
espaco = '  '
nItem = 0
nItem2 = 1

for cont in range(0,20):
    tr+= '--'
print(tr)
for cont in range(0,5):
    espaco += '  '
print(f'{espaco}LISTAGEM DE PREÇOS')
print(tr)

for i in range(0,(len(tupla))):
    print(tupla[nItem], end='')
    for j in range(0,(42 - len(tupla[nItem]) - len(tupla[nItem2])-1)):
        tr2 += '.'
    print(tr2, end='')
    print(tupla[nItem2])
    tr2 = '.'
    nItem += 2
    nItem2 += 2
    if nItem >= len(tupla):
        break
print(tr)

'''print(tupla[2], end='')
for cont in range(0,(42 - len(tupla[2]) - len(tupla[3])-1)):
    tr3 += '.'
print(tr3, end='')
print(tupla[3])'''

# tr3 = '.'

