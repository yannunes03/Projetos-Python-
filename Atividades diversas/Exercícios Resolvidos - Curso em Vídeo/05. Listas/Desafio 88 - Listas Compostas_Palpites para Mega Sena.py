'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa
vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

import random
from time import  sleep

print('-' * 30)
print('      JOGO NA MEGA SENA')
print('-' * 30)
nJogos = int(input('Quantos jogos você quer que eu sortei? '))
print(f'{"-=" *3} SORTEANDO {nJogos} JOGOS {"-=" *3}')

jogo = list()

for n in range(0,nJogos+1):
    for o in range(0,6):
        jogo.append(random.randint(1,60))
    print(f'Jogo{n}: {jogo}')
    sleep(1)
    jogo.clear()
print(f'{"-=" *5} < BOA SORTE! > {"-=" *5}')
