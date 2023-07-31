'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,
mostre: '''
# A) Quantas pessoas foram cadastrados.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

listaInicial = list()
listaCadastro = list()
confirmacao = ''

cont = 0
maiorPeso = menorPeso = 0

while True:
    cont += 1
    listaInicial.append(str(input(f'Insira o nome da {cont}ª pessoa da lista: ')))
    listaInicial.append(float(input('Qual o peso desta pessoa: ')))
    if len(listaCadastro) == 0:
        maiorPeso = menorPeso = listaInicial[1] # Guardando o peso
    else:
        if listaInicial[1] > maiorPeso:
            maiorPeso = listaInicial[1]
        if listaInicial[1] < menorPeso:
            menorPeso = listaInicial[1]
    listaCadastro.append(listaInicial[:])
    listaInicial.clear()

    confirmacao = input('Deseja Continuar? Digite (S) para sim ou (N) para não')
    if confirmacao == 'N':
        break

print(f'Ao todo você cadastrou {len(listaCadastro)} pessoas')
print(f'O maior peso foi de {maiorPeso}Kg. Peso de ', end='')
for p in listaCadastro:
    if p[1] == maiorPeso:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {menorPeso}Kg. Peso de ', end='')
for p in listaCadastro:
    if p[1] == menorPeso:
        print(f'[{p[0]}] ', end='')
print()


