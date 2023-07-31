x: float ; y: float ; z: float

print('Digite as três distancias: ')
x = input('Digite a distância de X: ')
y = input('Digite a distância de y: ')
z = input('Digite a distância de z: ')

if float(x) > float(y) and float(x) > float(y):
    print('A maior distância é X')
elif float(y) > float(x) and float(y) > float(z):
    print('A maior distância é y')
elif float(z) > float(x) and float(z) > float(y):
    print('A maior distância é z')
else:
    print('Empate')



