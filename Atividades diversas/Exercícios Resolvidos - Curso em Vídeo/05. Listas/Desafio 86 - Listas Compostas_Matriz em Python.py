'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta'''

listaPrincipal = [[0,0,0], [0,0,0], [0,0,0]]
cont = cont2 = 0

for x in range(0,3):
    for y in range(0,3):
        listaPrincipal[x][y] = int(input(f'Insira um valor para a posição [{x},{y}]: '))
print('A Matriz montada ficou da seguinte forma:')

for x in range(0,3):
    for y in range(0,3):
        print(f'[{listaPrincipal[x][y]}]', end='')
    print() #serve apenas para cancelar o 'end' uma vez que, após o término do 'for' em y, o 'end' fará com que iprima vazio após ele
