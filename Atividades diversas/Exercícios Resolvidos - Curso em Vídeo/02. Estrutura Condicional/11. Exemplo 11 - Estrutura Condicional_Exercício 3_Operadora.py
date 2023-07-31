'''
Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de telefone.
Cada minuto que exceder a franquia de 100 minutos custa R$ 2,00. Fazer um programa para ler a quantidade
de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago.
'''
minutos: int ; PrecoMinimo: int ;
ValorAPagar: float

PrecoMinimo = 50

minutos = input('Digite a quantidade de minutos: ')

if int(minutos) <= 100:
    ValorAPagar = int(PrecoMinimo)
else:
    ValorAPagar = int(PrecoMinimo) + 2 * (int(minutos)-100)

print(f'Valor a Pagar: R$ {ValorAPagar:.2f}')
