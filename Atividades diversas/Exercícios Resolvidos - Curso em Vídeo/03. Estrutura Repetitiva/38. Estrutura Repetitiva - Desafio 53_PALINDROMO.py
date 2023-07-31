'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
Desconsiderando os espaços'''

# ENTENDENDO A LÓGICA:

# O que é um palíndromo - Uma frase ou palavra que pode se ler da esquerda para direta ou vice-versa
# Ação 1 - colocar todas os caracteres em minúsculo
# Ação 2 - remover todos os espaços
# Ação 3 - Construir  conjunto de strings invertida
# Ação 4 - verificar se a string original e a invertida são iguais
# Ação 5 - se forem iguais, é um palíndromo. Se não, não é um palíndromo

string = str(input('Informe uma palavra ou string que iremos verificar se é um palíndromo ou não')).replace(' ','').strip().lower()

stringInvertida = string[len(string)-1]
n = 1

for cont in range(1,len(string)):
    n += 1
    stringInvertida = stringInvertida + string[len(string)-n]

if string == stringInvertida:
    print('A palavra ou frase informada É um caso de um palíndromo')
else:
    print('A palavra ou frase informada NÃO É um caso de um palíndromo')
