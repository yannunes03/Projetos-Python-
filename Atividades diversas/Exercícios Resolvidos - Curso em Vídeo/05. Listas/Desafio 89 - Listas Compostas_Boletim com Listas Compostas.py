'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.'''


dadosAluno = []
conjuntoAlunos = []
n = 1

while True:
    dadosAluno.append(input('Nome: '))
    dadosAluno.append(int(input(f'Nota {n}: ')))
    dadosAluno.append(int(input((f'Nota {n+1}: '))))
    continuar = input('Quer Continuar? [S/N]: ')
    conjuntoAlunos.append(dadosAluno[:])
    dadosAluno.clear()
    if continuar == 'N' or continuar == 'n':
        break
print('-=' * 30)
print('No.   NOME          MÉDIA')
print('-' * 30)

indice = 0

for o in conjuntoAlunos:
    print(f'{indice}', end='     ')
    indice += 1
    espaco = 20 - 6 - o[1]
    print(f'{o[0]}', end='')
    print(' ' * espaco, end='')
    media = int(o[1] + o[2]) / 2
    print(f'{media:.2f}')
