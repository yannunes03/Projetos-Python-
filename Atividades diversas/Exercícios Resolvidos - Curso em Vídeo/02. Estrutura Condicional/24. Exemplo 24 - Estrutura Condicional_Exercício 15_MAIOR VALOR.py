'''Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem'''

# O primeiro valor é maior
# o Segundo valor é maior
# Não existe valor maior, os dois são iguais

vermelho = '\033[0:31m'
azul = '\033[0:36m'
limpar = '\033[0m'

primeiroValor = float(input('{}Informe um valor para o primeiro número'.format(vermelho)))
segundoValor = float(input('{}Informe um valor para o segundo número'.format(azul)))

if  primeiroValor > segundoValor:
    str(print('{}O {}Primeiro {}valor é maior'.format(limpar,vermelho,limpar)))
elif primeiroValor < segundoValor:
    str(print('{}O {}Segundo {}valor é maior'.format(limpar,azul,limpar)))
else:
    str(print('{}Não existe valor maior, os dois são iguais'.format(limpar)))