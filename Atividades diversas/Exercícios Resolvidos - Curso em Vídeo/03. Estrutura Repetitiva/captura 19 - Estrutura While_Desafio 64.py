'''Crie um programa que leia vários números inteiros pelo teclado. O Programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag)'''

cont = soma = n = 0
n = 0

while n != 999:
    n = int(input('Digite um valor [digite 999 para parar]: '))
    soma += n
    cont += 1

print(f'Foram digitados {cont-1} números e a soma entre eles é igual a {soma-999}')