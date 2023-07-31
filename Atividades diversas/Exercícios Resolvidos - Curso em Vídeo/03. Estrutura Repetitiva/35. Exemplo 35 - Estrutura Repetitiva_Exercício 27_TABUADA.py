'''Mostre a tabuada de um número que o usuário escolher'''

multiplicador = int(input('Favor informe o número o qual você quer saber a tabuada?'))

for cont in range(1,11):
    resultado = multiplicador * cont
    print(f'{multiplicador} X {cont} = {resultado}')