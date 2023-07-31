'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantos já são maiores'''

n = 0
maiorIdade = 0
menorIdade = 0

for cont in range(0,7):
    n += 1
    idade = int(input('Informe o ano de nascimento da {}º pessoa?'.format(n)))
    if (2024 - idade) >= 18:
        maiorIdade += 1
    elif (2024 - idade) < 18:
        menorIdade += 1

print('Entre os anos informados, {} alcançaram a maioridade e {} ainda não'.format(maiorIdade, menorIdade))
