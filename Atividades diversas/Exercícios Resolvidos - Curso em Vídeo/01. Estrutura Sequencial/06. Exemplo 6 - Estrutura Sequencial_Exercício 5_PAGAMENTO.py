nome: str
ValorHora: float ; pagamento: float
HorasTrabalhadas: int

nome = input('Nome: ')
ValorHora = input('Valor por Hora: ')
HorasTrabalhadas = input('Horas trabalhadas: ')
pagamento = float(ValorHora) * float(HorasTrabalhadas)

#Escrituração de Dados | Placeholder | Forma atual, moderna e tendência

print('O pagamento para {} deve ser de R$ {:.2f}'.format(nome, pagamento))

#Escrituração de Dados | Interpolação | Forma mais simples e fácil

print(f'O pagamento para {nome} deve ser de R$ {pagamento:.2f}')

#Escrituração de Dados | Apenas Escriturando | Forma mais antiga, simples, porém em desuso

print(f'O pagamento para ', nome, ' dever ser de R$ ', pagamento)
