'''
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
mostrar o valor do troco a ser devolvido ao cliente.
'''

QuantidadeComprada: int
preco1: float ; DinheiroRecebido: float ; TROCO: float

preco1 = input('Preço Unitário do produto: R$ ')
QuantidadeComprada = input('Quantidade Comprada: ')
DinheiroRecebido = input('Dinheiro Recebido: ')

TROCO = float(DinheiroRecebido) - (float(preco1) * int(QuantidadeComprada))

#Escrituração de Dados | Placeholder | Forma atual, moderna e tendência

print('TROCO = {:.2f} '.format(TROCO))

#Escrituração de Dados | Interpolação | Forma mais simples e fácil

print(f'TROCO = {TROCO:.2f}')

#Escrituração de Dados | Apenas Escriturando | Forma mais antiga, simples, porém em desuso

print('TROCO = ', TROCO)