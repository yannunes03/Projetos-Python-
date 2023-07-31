'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''

import random

escolhaPC = ''
resultado = ''
nvitoria = 0


print('Vamos Jogar um PAR ou IMPAR?')

while True:
    escolha = str(input('Você escolhe PAR ou IMPAR?: ')).upper()
    if escolha != 'PAR' and escolha != 'par' and escolha != 'IMPAR' and escolha != 'impar':
        print('VALOR INVÁLIDO... Escolha (PAR) ou (IMPAR): ')
        continue
    num = int(input('Escolha um número entre 0 e 5: '))
    #Definição de quem será 'PAR' e quem 'Será IMPAR'
    if escolha == 'PAR' or escolha == 'par':
        escolhaPC = 'IMPAR'
    elif escolha == 'IMPAR' or 'impar':
        escolhaPC = 'PAR'

    numPC = random.randrange(0,5)

    soma = num + numPC

    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

    if resultado == escolha:
        nvitoria += 1
        print(f'você jogou {num} e o computador jogou {numPC}. O total deu {soma} e o resultado é {resultado}')
        print(f'você venceu pela {nvitoria}ª vez')
        print('Vamos jogar novamente...')
    else:
        print(f'você jogou {num} e o computador jogou {numPC}. O total deu {soma} e o resultado é {resultado}')
        break
print(f'GAME OVER! Você conquistou um total de {nvitoria} vitória(s)')






