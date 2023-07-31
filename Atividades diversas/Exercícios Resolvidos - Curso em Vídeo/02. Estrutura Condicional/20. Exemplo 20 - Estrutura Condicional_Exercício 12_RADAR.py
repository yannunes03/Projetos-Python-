'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
'''

velocidadeRegistrada = int(input('Por favor, informe a velocidade registrada?'))

if velocidadeRegistrada > 80:
    print('VOCÊ ESTÁ MULTADO!')
    print('Você ultrapassou a velocidade máxima permitida, de 80 Km/h.')
    print('A multa vai custar R$ 7,00 por cada Km acima do limite')
    print(int(velocidadeRegistrada * 7))
else:
    print('Tudo ok')