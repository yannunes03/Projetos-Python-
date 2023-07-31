'''Crie um programa que leia dois valores e mostre um menu na tela:'''

'''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso.
'''

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
acao = 0
resultado = 0
print('O que deseja fazer com esses números?')

while True:
    print('Digita a ação desejada: ')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    acao = int(input('Ação: '))
    if acao == 1:
        print('Ação selecionada: SOMA')
        resultado = n1 + n2
        print(f'A soma dos dois valores é {resultado}')
    elif acao == 2:
        print('Ação selecionada: MULTIPLICAÇÃO')
        resultado = n1 * n2
        print(f'O resultado da multiplicação dos dois valores é {resultado}')
    elif acao == 3:
        print('Ação selecionada: MAIOR VALOR')
        if n1 > n2:
            print(f'O maior valor é {n1}')
        if n2 > n1:
            print(f'O maior valor é {n2}')
        if n1 == n2:
            print(f'Não existe maior valor, ambos são iguais')
    elif acao ==4:
        print('Ação selecionada: NOVOS NÚMEROS')
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
        continue
    elif acao == 5:
        print('Ação selecionada: SAIR DO PROGRAMA')
        print('FIM DO PROGRAMA')
        break





