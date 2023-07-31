'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''


while True:
    multiplicador = int(input('Favor informe o número o qual você quer saber a tabuada?'))
    if multiplicador < 0:
        print('Multiplicador inválido. FIM DO PROGRAMA')
        break
    print('-----TABUADA DE {} -----'.format(multiplicador))
    for cont in range(1,11):
        resultado = multiplicador * cont
        print(f'{multiplicador} X {cont} = {resultado}')