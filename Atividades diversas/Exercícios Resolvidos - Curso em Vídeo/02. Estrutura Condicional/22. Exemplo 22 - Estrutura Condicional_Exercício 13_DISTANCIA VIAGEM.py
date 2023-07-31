'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50
por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas
'''

distanciaViagem = int(input('Por favor, informe qual foi a distância da viagem realizada'))

if distanciaViagem < 200:
    custoViagem = 0.50
    custoTotal = distanciaViagem * custoViagem
    print(f'O custo total da viagem foi de {custoTotal:.2f}')
else:
    custoViagem = 0.45
    custoTotal = distanciaViagem * custoViagem
    print(f'O custo total da viagem foi de {custoTotal:.2f}')


