'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares
em ordem crescente'''

listaPrincipal = []
listaPares = list()
listaImpares = list()
valor = ''

for cont in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0: #adicionando valores pares à lista de pares.
        listaPares.append(valor)
    elif valor % 2 != 0: #adicionando valores ímpares à lista de pares.
        listaImpares.append(valor)
listaPrincipal.append(sorted(listaPares[:]))
listaPrincipal.append(sorted(listaImpares[:]))

print(listaPrincipal)
print(f'Os valores pares foram {listaPrincipal[0]}')
print(f'Os valores ímpares foram {listaPrincipal[1]}')
