'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o
vencedor tirou o maior número no dado'''

import random
from time import sleep
from operator import itemgetter

dicionario = {}

for n in range(1,5):
    dicionario[f'jogador{n}'] = random.randrange(1,6)

print(dicionario)

for key,value in dicionario.items():
    print(f'O {key} tirou {value} no dado')
    sleep(1)

ranking = list()
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' == RANKING DOS JOGADORES ==')
for indice, valor in enumerate(ranking):
    print(f' {indice+1}º lugar: {valor[0]} com {valor[1]}.')
    sleep(1)
