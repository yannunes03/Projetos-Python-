'''
Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo médio
do carro, com três casas decimais.
'''

distancia: int;
CombustivelGasto: float ; ConsumoMedio: float

distancia = int(input('Distância Percorrida (KM): '))
CombustivelGasto = int(input('Combustível Gasto (L): '))
ConsumoMedio = int(distancia) / float(CombustivelGasto)

#Escrituração de Dados | Placeholder | Forma atual, moderna e tendência

print('Consumo Médio = {:.2f} Km/L'.format(ConsumoMedio))

#Escrituração de Dados | Interpolação | Forma mais simples e fácil

print(f'Consumo Médio = {ConsumoMedio:.2f} Km/L')

#Escrituração de Dados | Apenas Escriturando | Forma mais antiga, simples, porém em desuso

print('Consumo Médio = ', ConsumoMedio, ' Km/L')