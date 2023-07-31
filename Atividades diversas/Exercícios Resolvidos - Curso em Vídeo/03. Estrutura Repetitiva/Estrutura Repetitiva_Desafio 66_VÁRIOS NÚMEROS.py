'''Crie um programa que leia vários número inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''

contador = 0
soma = 0

while True:
    n = int(input('Digite um número'))
    if n == 999:
        break
    contador += 1
    soma += n
    #O Contador adiciona mais '1' e a soma considera o número informada depois que a condição de parada é testada

print(f'A quantidade de números digitados foi de {contador}, e a sua soma foi de {soma}')
