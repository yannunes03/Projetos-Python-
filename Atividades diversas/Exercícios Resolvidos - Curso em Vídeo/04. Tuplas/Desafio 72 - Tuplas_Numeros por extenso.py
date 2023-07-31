'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte'''

#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numerosPorExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
                     'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
                     'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Informe um número de 1 a 20 para que possamos retornar ele por extenso'))
    if numero < 0 or numero > 20: #Caso o usuário digite um número que esteja fora do range
        print('Número inválido. tente novamente')
    else:
        print(f'O número informado por extenso é {numerosPorExtenso[numero]}')
        confirmacao = str(input('Quer continuar? [S/N]'))
        while confirmacao != 'S' and confirmacao != 'N': # Caso o usuário não digite S ou N para confirmar a continuação do programa
            confirmacao = str(input('Comando inválido. Digite (S) para Sim ou (N) para não'))
            if confirmacao == 'S':
                continue
            elif confirmacao == 'N':
                break
        if  confirmacao == 'N':
            print('FIM DO PROGRAMA')
            break

