x: int ; y: int

print('Digite dois números: ')
x = int(input('Digite um número para x: '))
y = int(input('Digite um número para y: '))

while x != y:
    if x > y:
        print('DECRESCENTE')
        print('Digite outros dois números: ')
        x = int(input('Digite um número para x: '))
        y = int(input('Digite um número para y: '))
    elif x < y:
        print('CRESCENTE')
        print('Digite outros dois números: ')
        x = int(input('Digite um número para x: '))

