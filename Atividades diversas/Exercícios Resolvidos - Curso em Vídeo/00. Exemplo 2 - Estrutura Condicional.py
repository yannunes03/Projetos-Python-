x: float ; y: float ; z: float

x = input('Digite a primeira nota: ')
y = input('Digite a segunda nota: ')
z = float(x) + float(y)

#Escrituração de Dados | Placeholder | Forma atual, moderna e tendência
print('NOTA FINAL = {z:.2f}'.format(z))

if z < 60 :
    print('REPROVADO!')
else:
    print('APROVADO!')

#Escrituração de Dados | Interpolação | Forma mais simples e fácil
print(f'NOTA FINAL = {z:.2f}')

if z < 60 :
    print('REPROVADO!')
else:
    print('APROVADO!')

#Escrituração de Dados | Apenas Escriturando | Forma mais antiga, simples, porém em desuso
print('NOTA FINAL = ', z)

if z < 60 :
    print('REPROVADO!')
else:
    print('APROVADO!')
