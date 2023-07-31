'''
Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um indivído.
O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular e imprimir
a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez, mostrar a
mensagem "IMPOSSÍVEL CALCULAR"
'''


x: float ; ContIdades: float; Soma:float

ContIdades = 0
Soma = 0

print('Digite as idades: ')
x = float(input())

while x >= 0:
    ContIdades = ContIdades + 1
    Soma = Soma + x
    x = float(input())


if Soma == 0:
    print('IMPOSSÍVEL CALCULAR')
else:
    print('Média = ', Soma / ContIdades)





