'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa
deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

nMaior = nMenor = cont = soma = 0
continuar = ''

while True:
    num = int(input('Digite um valor: '))
    cont += 1
    if cont <= 1:
        nMenor = num
    soma += num
    media = soma / cont
    if num > nMaior:
        nMaior = num
    if num < nMenor:
        nMenor = num
    print(f'Foram digitado um total de {cont} números')
    print(f'A soma entre eles foi de {soma}')
    print(f'A média entre todos os números é {media}')
    print(f'O maior valor digitado foi o {nMaior}')
    print(f'O menor valor digitado foi de {nMenor}')
    continuar = str(input('Deseja Continuar [S/N]: '))
    if  continuar == 'N' or continuar == 'n':
        break
