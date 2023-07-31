'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os e
cadastre-os em uma lista. Caso o número já exista lá dentro ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente'''

lista = []

while True:
    num = int(input('Digite um valor para que este seja adicionado à lista'))
    if num not in lista:
        lista.append(num)
    elif num in lista:
        print('Valo duplicado! Não vou adicionar...')
    continuar = str(input('Deseja Continuar? Pressione (S) para sim ou (N) para não?'))
    if continuar == 'S' or continuar == 's':
        continue
    elif continuar == 'N' or continuar =='n':
        print('FIM DO PROGRAMA')
        break
    else:
        while continuar != 'S' and continuar !='s' and continuar != 'N' and continuar != 'n':
            print('Valor inválido...Tente Novamente...')
            continuar = str(input('Pressione (S) para sim ou (N) para não'))
    if continuar == 'S' or continuar == 's':
        continue
    elif continuar == 'N' or continuar == 'n':
        break
print(sorted(lista))