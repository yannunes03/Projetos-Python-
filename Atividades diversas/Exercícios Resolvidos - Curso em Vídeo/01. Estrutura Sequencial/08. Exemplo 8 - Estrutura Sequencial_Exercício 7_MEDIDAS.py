A: float; B: float; C: float; AreaQuadrado: float; AreaTriangulo: float; AreaTrapezio: float

A = input('Digite a medida A: ')
B = input('Digite a medida B: ')
C = input('Digite a medida C: ')

AreaQuadrado = float(A) * float(A)
AreaTriangulo = (float(A) * float(B) / 2)
AreaTrapezio = (((float(A) + float(B)) * float(C)) / 2)

#Escrituração de Dados | Placeholder | Forma atual, moderna e tendência

print('AREA DO QUADRADO = {:.4f}'.format(AreaQuadrado))
print('AREA DO TRIANGULO = {:.4f}'.format(AreaTriangulo))
print('AREA DO TRAPÉZIO = {:.4f}'.format(AreaTrapezio))

#Escrituração de Dados | Interpolação | Forma mais simples e fácil

print(f'AREA DO QUADRADO = {AreaQuadrado:.4f}')
print(f'AREA DO TRIANGULO = {AreaTriangulo:.4f}')
print(f'AREA DO TRAPÉZIO = {AreaTrapezio:.4f}')

#Escrituração de Dados | Apenas Escriturando | Forma mais antiga, simples, porém em desuso

print('AREA DO QUADRADO = ', AreaQuadrado )
print('AREA DO TRIANGULO = ', AreaTriangulo)
print('AREA DO TRAPÉZIO = ', AreaTrapezio)

