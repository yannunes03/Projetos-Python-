'''
Ler um número inteiro N, daí mstrar na tela a tabuada de N para 1 a 10
'''

N: int ; x: int

x = int(input('Deseja a tabuada para qual valor ?'))

# Escrituração de Dados | Placeholder | Forma atual, moderna e tendência
for N in range(1,10):
    print('{} X {} = '.format(x,N,x,N), x * N)
print()

# Escrituração de Dados | Interpolação | Forma mais simples e fácil
for N in range(1, 10):
    print(f'{x} X {N} = ', x * N)
print()

#Escrituração de Dados | Apenas Escriturando | Forma mais antiga, simples, porém em desuso
for N in range(1, 10):
    print(x, ' X ', N, ' = ', x * N)
print()




