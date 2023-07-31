x: int ; y: int ; troca: int ; soma: int ; i: int

print('Digite dois números: ')
x = int(input('Digite o 1º número: '))
y = int(input('Digite o 2º número: '))

if x > y:
    troca = x
    x = y
    y = troca

soma = 0
i = 0

for i in range (x,y):
    if i % 2 != 0:
        soma = soma + i
print('SOMA DOS IMPARES = {}'.format(soma))
