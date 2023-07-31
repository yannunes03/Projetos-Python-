'''Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequência de Fibonacci'''

# A sequência de Fibonnaci é uma sequ~encia de números, onde o número 1 é o primeiro e segundo termo da ordem
# e os demais são originados pela soma de seus antecessores

#Exemplo: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

nElementos = int(input('Informe um número para que possamos lhe revelar a sua sequência de Fibonacci'))
cont = 0
antecessor1 = 1
antecessor2 = 0
sequencia = str(f'{antecessor2} -> {antecessor1}')

while cont <= nElementos - 3:
    soma = antecessor1 + antecessor2
    sequencia = sequencia + str(f' -> {soma}')
    antecessor2 = antecessor1
    antecessor1 = soma
    cont += 1
print(sequencia, end='')
print(' -> FIM')



