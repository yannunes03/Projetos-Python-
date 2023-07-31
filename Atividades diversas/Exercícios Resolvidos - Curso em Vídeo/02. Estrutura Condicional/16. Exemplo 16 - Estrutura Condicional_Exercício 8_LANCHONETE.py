'''
Uma lanchonete possui vários Produtos. Cada produto possui um código e um preço. Você deve fazer um
programa para ler o código e a quantidade comprada de um produto (suponha um código válido), e daí
informar qual o valor a ser pago, com duas casas decimais.
'''


codigo = int ; quantidade: int
ValorAPagar = float

codigo = int(input('Codigo do produto comprado: '))
quantidade = int(input('Quantidade comprada: '))

if codigo == 1:
    ValorAPagar = 5 * quantidade
elif codigo == 2:
    ValorAPagar = 3.50 * quantidade
elif codigo == 3:
    ValorAPagar = 4.80 * quantidade
elif codigo == 4:
    ValorAPagar = 8.90 * quantidade
elif codigo == 5:
    ValorAPagar = 7.32 * quantidade

print('Valor a pagar: R$ {:.2f}'.format(ValorAPagar))

