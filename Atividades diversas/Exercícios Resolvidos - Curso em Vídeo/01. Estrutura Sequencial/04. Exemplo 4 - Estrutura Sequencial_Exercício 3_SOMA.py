'''
Fazer um programa para ler dois valores inteiros X e Y, e depois mostrar na tela o valor da soma destes
números
'''

valor1: int ; valor2: int ; soma: int
valorx: str ; valory: str

valorx = input('Digite o valor de X: ')
valory = input('Digite o valor de y: ')

valor1 = int(valorx)
valor2 = int(valory)
soma = int(valor1) + int(valor2)

#Escrituração de Dados | Placeholder | Forma atual, moderna e tendência

print('SOMA = {}'.format(soma))

#Escrituração de Dados | Interpolação | Forma mais simples e fácil

print(f'SOMA = {soma}')

#Escrituração de Dados | Apenas Escriturando | Forma mais antiga, simples, porém em desuso

print('SOMA = ', soma)