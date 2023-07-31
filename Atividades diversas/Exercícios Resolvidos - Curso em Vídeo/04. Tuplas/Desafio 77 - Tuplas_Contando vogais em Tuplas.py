'''Crie um programa que tenha uma tupla com várias palavras.
Depois disso, você deve mostrar para cada palavra, quais são as suas vogais'''

tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
         'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

vogais = ('A', 'E', 'I', 'O', 'U')
conjVogais = ''
cont = 0


for i in tupla: # Percorrendo cada uma das palavras na Tupla
    cont = len(i)
    print(f'Na palavra {i} temos as seguintes vogais: ', end='')
    for j in range(0,len(i)): # Percorrendo cada string em cada palavra
        if i[j] in vogais: # verificando se cada string é uma vogal
            conjVogais += i[j].lower() + ' '
    print(conjVogais)
    conjVogais = ''
