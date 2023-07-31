'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta'''

# Aprimore o desafio anterior, mostrando no final:

# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha

listaPrincipal = [[0,0,0], [0,0,0], [0,0,0]]
cont = cont2 = 0
somaPares = 0
somaParesColuna3 = 0
maiorValorLinha2 = 0

for x in range(0,3):
    for y in range(0,3):
        listaPrincipal[x][y] = int(input(f'Insira um valor para a posição [{x},{y}]: '))
        if listaPrincipal[x][y] % 2 == 0:
            somaPares += listaPrincipal[x][y]
            if y == 2:
                somaParesColuna3 += listaPrincipal[x][y]
        if x == 1 and listaPrincipal[x][y] > maiorValorLinha2:
            maiorValorLinha2 = listaPrincipal[x][y]

print('A Matriz montada ficou da seguinte forma:')


for x in range(0,3):
    for y in range(0,3):
        print(f'[{listaPrincipal[x][y]}]', end='')
    print() #serve apenas para cancelar o 'end' uma vez que, após o término do 'for' em y, o 'end' fará com que iprima vazio após ele
print(f'A soma de todos os valores pares lançados na matriz foi igual a {somaPares}')
print(f'A soma de todos os valores pares lançados na 3ª coluna da matriz é igual a {somaParesColuna3}')
print(f'O maior valor lançado na 2ª linha foi o {maiorValorLinha2}')



