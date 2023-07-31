'''
Fazer um programa para ler a quantidade de glicose no sangue de uma pessoa e depois mostrar na tela a
classificação desta glicose de acordo com a tabela de referência ao lado.
'''

glicose: float

glicose = input('Digite a medidade da glicose: ')

if float(glicose) <= 100:
    print('Classificação : normal')
else:
    if float(glicose) > 100 and float(glicose) <=140:
        print("Classificação : Elevado")
    else:
        print("Classificação : Diabetes")