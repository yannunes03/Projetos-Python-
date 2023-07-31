'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F. Caso esteja errado, peça a
digitação novamente até ter um valor correto'''

sexo: str

sexo = str(input('Favor informe qual o seu sexo. Informe (M) caso seja masculino ou (F) caso seja feminino'))

while sexo != 'M' and sexo != 'F' and sexo != 'm' and sexo !='f':
    print('Valor incorreto, digite novamente')
    sexo = input('Informe seu sexo por favor?')

print('Obrigado, e um bom dia')