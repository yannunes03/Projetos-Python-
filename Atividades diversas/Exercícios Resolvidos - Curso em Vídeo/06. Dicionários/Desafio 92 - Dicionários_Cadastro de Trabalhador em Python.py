'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
(com idade) em um dicionário se por acaso o CTPS for diferente de ZERO, o dicionário receberá
também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa
vai se aposentar'''

from datetime import datetime

cadastro = {'Nome': '',
            'Ano de Nascimento': 0,
            'Carteira de trabalho': 00000}

cadastro['Nome'] = str(input('Nome: '))
cadastro['Ano de Nascimento'] = int(input('Ano de Nascimento (4 dígitos): '))
cadastro['Idade'] = datetime.now().year - cadastro['Ano de Nascimento']
cadastro['Carteira de trabalho'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['Carteira de trabalho'] != 0:
    cadastro['Ano de Contratação'] = int(input('Ano de Contratação (4 dígitos): '))
    cadastro['Salário'] = float(input('Salário: R$ '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Ano de Contratação'] + 35) - datetime.now().year)
print(cadastro)

print('-=' * 20)
print(f"nome tem o valor {cadastro['Nome']}")
print(f"idade tem o valor {cadastro['Idade']}")
print(f"ctps tem o valor {cadastro['Carteira de trabalho']}")
print(f"contratação tem o valor de {cadastro['Ano de Contratação']}")
print(f"salário tem o valor de {cadastro['Salário']}")
print(f"aposentadoria tem o valor de {cadastro['Aposentadoria']}")


