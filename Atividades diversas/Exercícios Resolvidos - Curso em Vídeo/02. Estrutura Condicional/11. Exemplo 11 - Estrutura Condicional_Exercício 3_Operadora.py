minutos: int ; PrecoMinimo: int ;
ValorAPagar: float

PrecoMinimo = 50

minutos = input('Digite a quantidade de minutos: ')

if int(minutos) <= 100:
    ValorAPagar = int(PrecoMinimo)
else:
    ValorAPagar = int(PrecoMinimo) + 2 * (int(minutos)-100)

print(f'Valor a Pagar: R$ {ValorAPagar:.2f}')
