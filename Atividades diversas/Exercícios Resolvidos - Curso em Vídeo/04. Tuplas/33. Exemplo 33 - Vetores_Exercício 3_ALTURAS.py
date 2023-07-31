'''
Fazer um programa para ler nome, idade e altura de N pessoas. Depois, mostrar na tela a altura média
das pessoas, e mostrar também a porcentagem de pessoas com menos de 16 anos, bem como os nomes dessas
pessoas caso houver
'''



N: int ; idade: int ; numero: int
nome: str
altura: float ; media: float ; menor: float ; AlturaTotal: float

N = int(input('Quantas pessoas serão digitadas? '))
Nom: [float] = [0 for x in range(N)]
Idad: [float] = [0 for x in range(N)]
Alt: [float] = [0 for x in range(N)]

numero = 1
AlturaTotal = 0
menor = 0

for i in range(0,N):
    nome = str(input(f'Dados da {numero}ª pessoa: '))
    numero = numero + 1
    Nom[i] = nome

    idade = int(input('Idade: '))
    Idad[i] = idade

    altura = float(input('Altura: '))
    Alt[i] = altura

    AlturaTotal = AlturaTotal + altura

    if idade < 16:
        menor = menor + 1

media = AlturaTotal / N

print(f'Altura média: {media:.2f}')
print(f'Pessoas com menos de 16 anos: {(menor/N)*100} %')
print('São elas: ')

for i in range (0,N):
    if Idad[i] < 16:
        print(Nom[i])