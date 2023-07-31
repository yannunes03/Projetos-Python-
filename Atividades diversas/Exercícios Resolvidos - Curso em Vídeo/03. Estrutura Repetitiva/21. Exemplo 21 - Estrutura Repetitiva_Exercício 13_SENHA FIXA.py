'''
Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada letitura de
senha incorreta informada, escrever a mensagem "Senha Invalida!" Tente novamente:". Quando a senha for
informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere
que a senha correta é o valor 2002.
'''

senha: int

senha = int(input('Digite a Senha: '))

while senha != 2022:
    senha = int(input('Senha Inválida! Tente Novamente: '))

print('Acesso Liberado!')
