'''
Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
 qual foi o número escolhido pelo computador.

 O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint

numeroPC = int(randint(0,5))

print('Vamos jogar um jogo de adivinhação? Tente adivinhar o número gerado pelo computador')
numeroUsuario = int(input('Por favor, digite um número inteiro entre 0 e 5'))

if numeroUsuario == numeroPC:
    print('Você adivinhou, você GANHOU!')
else:
    print('que pena, você errou, então PERDEU')
