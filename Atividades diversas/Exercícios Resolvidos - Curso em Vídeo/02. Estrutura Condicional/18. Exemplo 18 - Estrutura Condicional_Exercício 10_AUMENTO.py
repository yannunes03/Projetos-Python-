salario: float; Nsalario: float ; aumento: float
porcentagem: str

salario = float(input('Digite o salario da pessoa: '))

if salario  <= 1000:
    Nsalario = (salario * 0.2) + salario
    aumento = Nsalario - salario
    porcentagem = '20%'
elif salario > 1000 and salario <= 3000:
    Nsalario = (salario * 0.15) + salario
    aumento = Nsalario - salario
    porcentagem = '15%'
elif salario > 3000 and salario <= 8000:
    Nsalario = (salario * 0.1) + salario
    aumento = Nsalario - salario
    porcentagem = '10%'
elif salario > 8000:
    Nsalario = (salario * 0.05) + salario
    aumento = Nsalario - salario
    porcentagem = '5%'

#Escrituração de Dados | Placeholder | Forma atual, moderna e tendência

print('Novo salario = R$ {:.2f}'.format(Nsalario))
print('Aumento = R$ {:.2f}'.format(aumento))
print('Porcentagem = {}'.format(porcentagem))

#Escrituração de Dados | Interpolação | Forma mais simples e fácil

print(f'Novo salario = R$ {Nsalario:.2f}')
print(f'Aumento = R$ {aumento:.2f}')
print(f'Porcentagem = {porcentagem}')

#Escrituração de Dados | Apenas Escriturando | Forma mais antiga, simples, porém em desuso

print('Novo salario = R$ ', Nsalario)
print('Aumento = R$ ', aumento)
print('Porcentagem = ', porcentagem)




