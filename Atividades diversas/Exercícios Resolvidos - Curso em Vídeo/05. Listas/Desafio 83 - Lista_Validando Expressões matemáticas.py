'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
deverá analisar se a expressão passa está com os parênteses abertos e fechados na ordem correta.'''

lista = list()

expressao = str(input('Digite a expressão: '))


for n in range(0,len(expressao)):
    lista.append(expressao[n])
print(lista)
pAberto = lista.count('(')
pFechado = lista.count(')')
if pAberto == pFechado:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')