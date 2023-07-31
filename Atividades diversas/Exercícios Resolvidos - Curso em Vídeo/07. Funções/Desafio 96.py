'''Faça um programa que tenha uma função chamada área(), que recebe as dimenssões de um terreno retangular (largura e
comprimento) e mostre a área do terreno'''

def area(larg, comp):
    a = larg * comp
    print(f'A Área de um terreno {larg:.2f}mX{comp:.2f} é de {a}m².')



#Programa principal
print('Controle de Terrenos')
print('-' * 20)

largura = float(input('Informe a LARGURA (m): '))
comprimento = float(input('Informe o Comprimento (m): '))
area(largura, comprimento)














