'''Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa deve encerrar quando ele disse que quer mostrar os termos.'''

termo1 = int(input('Defina o 1º termo da progressão aritmética'))
razao = int(input('Qual será a razão desta progressão aritmética?'))

soma = termo1
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(soma), end= '')
        soma += razao
        cont+= 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')







