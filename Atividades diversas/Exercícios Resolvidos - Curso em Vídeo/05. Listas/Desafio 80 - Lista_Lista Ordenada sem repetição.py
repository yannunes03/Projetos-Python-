'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em
uma lista, já na posição correta de inserção (sem usar o sort().'''

# No final, mostre a lista ordenada na tela.

# O que fazer:
# adicionar os maiores valores sempre próximo do final
# - se um número for maior que o valor valor, adicioná-lo depois desse maior valor com o uso do append
# - se um número for menor que o menor valor, adicioná-lo antes desse maior valor.
# adicionar os menores valores sempre próximo do início:
# - Se um número for menor que o menor valor, adicioná-lo antes dele na posição da lista

lista = []


for c in range(0,5):
    n = int(input(f'Digite um valor: '))
    if  c == 0 or n > lista[-1]:
        lista.append(n)
    else :
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')


