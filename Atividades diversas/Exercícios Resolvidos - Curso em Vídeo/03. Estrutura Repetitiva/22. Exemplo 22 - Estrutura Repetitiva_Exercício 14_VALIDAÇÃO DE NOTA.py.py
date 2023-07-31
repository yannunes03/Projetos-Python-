PrimeiraNota: float ; SegundaNota: float ; media: float

PrimeiraNota = float(input('Digite a primeira nota: '))

while PrimeiraNota < 0 or PrimeiraNota > 10:
    PrimeiraNota = float(input('Valor invalido! Tente novamente: '))

SegundaNota = float(input('Digite a segunda nota: '))

while SegundaNota < 0 or SegundaNota > 10:
    SegundaNota = float(input('Valor invalido! Tente novamente: '))

media = (PrimeiraNota + SegundaNota) / 2

#Escrituração de Dados | Placeholder | Forma atual, moderna e tendência

print('MÉDIA = {:.2F}'.format(media))

#Escrituração de Dados | Interpolação | Forma mais simples e fácil
print(f'MÉDIA = {media:.2f})

#Escrituração de Dados | Apenas Escriturando | Forma mais antiga, simples, porém em desuso
print('MÉDIA = ', media )