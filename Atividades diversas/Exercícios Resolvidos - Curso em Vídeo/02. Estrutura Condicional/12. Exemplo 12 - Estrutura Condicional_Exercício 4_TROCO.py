'''
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o valor
restante
'''

x: float ; z: float ; ValorAPagar: float ; resultado: float
y: int

x = input('Preço Unitário do Produto: ')
y = input('Quantidade comprada: ')
z = input('Dinheiro Recebido: ')

ValorAPagar = float(x) * float(y)

#Escrituração de Dados | Placeholder | Forma atual, moderna e tendência
if float(z) > float(ValorAPagar):
    resultado = float(z) - float(ValorAPagar)
    print('TROCO = {:.2f}'.forma(resultado))
else:
    if  float(z) < float(ValorAPagar):
        resultado = float(ValorAPagar) - float(z)
        print('DINHEIRO INSUFICIENTE. FALTAM R$ {:.2f}'.format(resultado))
    else:
        print('NÃO HÁ TROCO OU VALOR FALTANDO PARA PAGAMENTO')

#Escrituração de Dados | Interpolação | Forma mais simples e fácil
if float(z) > float(ValorAPagar):
    resultado = float(z) - float(ValorAPagar)
    print(f'TROCO = {resultado:.2f} ')
else:
    if  float(z) < float(ValorAPagar):
        resultado = float(ValorAPagar) - float(z)
        print(f'DINHEIRO INSUFICIENTE. FALTAM R$ {resultado:.2f}')
    else:
        print('NÃO HÁ TROCO OU VALOR FALTANDO PARA PAGAMENTO')

#Escrituração de Dados | Apenas Escriturando | Forma mais antiga, simples, porém em desuso
if float(z) > float(ValorAPagar):
    resultado = float(z) - float(ValorAPagar)
    print(f'TROCO = {resultado:.2f} ')
else:
    if  float(z) < float(ValorAPagar):
        resultado = float(ValorAPagar) - float(z)
        print('DINHEIRO INSUFICIENTE. FALTAM R$ ', resultado)
    else:
        print('NÃO HÁ TROCO OU VALOR FALTANDO PARA PAGAMENTO')
