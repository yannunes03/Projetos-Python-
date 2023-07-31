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





