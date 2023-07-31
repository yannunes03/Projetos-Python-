'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:'''
# A média de idade do grupo.
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos.

somaIdade = contMulheres = maisVelho = 0
nomeVelho: ''


for numero in range(1,5):
    print(F'-----{numero}ª PESSOA-----')
    nome = str(input(f'Informe o nome da {numero}º pessoa: '))
    idade = int(input('Informe a idade desta pessoa: '))
    sexo = str(input('Informe o sexo desta pessoa. Digite (M) para Homem e (F) para Mulher: '))

    somaIdade += idade
    if sexo == 'M' and idade < 20:
        contMulheres += 1
    elif sexo == 'M':
        idadeHomem = idade
        if idadeHomem > maisVelho:
            maisVelho = idadeHomem
            nomeVelho = nome

media = somaIdade / 4
print(f'A média de idade do grupo é de {media} anos')
print(f'O homem mais velho possui uma idade de {maisVelho}, e seu nome é {nomeVelho}')
print(f'A quantidade de mulheres que têm menos de 20 anos é de {contMulheres}')


