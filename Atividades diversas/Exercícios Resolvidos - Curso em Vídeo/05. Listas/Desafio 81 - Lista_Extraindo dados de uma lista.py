'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: '''

# A) Quantos números foram digitados
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = list()
continuar = ''

lista.append(int(input('Digite um número: ')))
while True:
    continuar = input(str('Deseja Continuar [S/N]: '))
    if continuar == 'N' or continuar == 'n':
        break
    elif continuar == 'S' or continuar == 's':
        lista.append(int(input('Digite um número: ')))
    elif continuar != 'S' or continuar != 's':
        continuar = print('Valor inválido...', end=' ')


print(lista)
print(f'Ao todo foram digitado {len(lista)} números')
print(f'A lista de valores ordenada de forma decrescente fica da seguinte forma {sorted(lista, reverse= True)}')

if 5 in lista:
    print('O número 5 foi digitado e incluído na lista')
elif 5 not in lista:
    print('O número 5 não foi digitado e não está na lista')





