'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela.'''

dicionario = dict()

dicionario['nome'] = input('Nome: ')
dicionario['Média'] = float(input(f"Média do {dicionario['nome']}: "))

print(f"- O Nome é igual a {dicionario['nome']}")
print(f"- A média é igual a {dicionario['Média']}")
if dicionario['Média'] >= 7:
    print('- Situação é igual a Aprovado')
else:
    print('- Situação é igual a Reprovado')
