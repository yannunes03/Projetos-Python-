'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então empréstimo
será negado.
'''

valorCasa = float(input('Qual o valor da Casa?'))
salarioComprador = float(input('Qual o seu salário?'))
periodoPagamento = float(input('Em quantos anos você pretende pagar?'))
prestacaoMensal = float(valorCasa / (12 * periodoPagamento))

# Se o valor da prestação mensal for menor que 30% do salário, o empréstimo será feito

if  prestacaoMensal < (salarioComprador * 0.3):
    print(str('EMPRÉSTIMO CONCEDIDO'))
else:
    print(str(f'EMPRÉSTIMO NEGADO. O Valor da prestação mensal (R${prestacaoMensal:.0f}) excede o valor de 30% ({(salarioComprador * 0.3):.0f}) de seu salário ({salarioComprador:.0f})'))