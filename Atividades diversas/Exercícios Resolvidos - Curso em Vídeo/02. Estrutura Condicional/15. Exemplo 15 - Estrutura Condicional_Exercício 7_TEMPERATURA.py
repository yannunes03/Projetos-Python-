escala: str
y: float ; temperatura: float ; celsius: float ; fahrenheit: float

escala = input('Voce vai digitar a temperatura em qual escala (C/F)? ')

#Escrituração de Dados | Placeholder | Forma atual, moderna e tendência
if str(escala) == 'F':
    temperatura = input('Digite a temperatura em Fahrenheit: ')
    celsius = 5/9 * (float(temperatura) - 32)
    print('Temperatura equivalente em Celsius: {:.0F} ºC'.format(celsius))
elif str(escala) == 'C':
    temperatura = input('Digite a temperatura Celsius:')
    fahrenheit = float(temperatura) * 9/5 + 32
    print('Temperatura equivalente em fahrenheit: {:.0f} ºF'.format(fahrenheit))

#Escrituração de Dados | Interpolação | Forma mais simples e fácil
if str(escala) == 'F':
    temperatura = input('Digite a temperatura em Fahrenheit: ')
    celsius = 5/9 * (float(temperatura) - 32)
    print(f'Temperatura equivalente em Celsius: {celsius:.0F} ºC')
elif str(escala) == 'C':
    temperatura = input('Digite a temperatura Celsius:')
    fahrenheit = float(temperatura) * 9/5 + 32
    print(f'Temperatura equivalente em fahrenheit: {fahrenheit:.0f} ºF')

#Escrituração de Dados | Apenas Escriturando | Forma mais antiga, simples, porém em desuso
if str(escala) == 'F':
    temperatura = input('Digite a temperatura em Fahrenheit: ')
    celsius = 5/9 * (float(temperatura) - 32)
    print('Temperatura equivalente em Celsius: ', celsius, ' ºC')
elif str(escala) == 'C':
    temperatura = input('Digite a temperatura Celsius:')
    fahrenheit = float(temperatura) * 9/5 + 32
    print('Temperatura equivalente em fahrenheit: ', fahrenheit, ' ºF')

