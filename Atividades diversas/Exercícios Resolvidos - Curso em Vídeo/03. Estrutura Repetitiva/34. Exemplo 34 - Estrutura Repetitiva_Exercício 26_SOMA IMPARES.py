'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três,
e que se encontram no intervalo de 1 até 500.'''

# Números mútliplos: números que são resultados de outros números.

from time import sleep

soma = 0
contNumeros = 0

for cont in range(1,501):
    if cont % 2 != 0 and cont % 3 == 0:
        contNumeros = contNumeros + 1
        soma = soma + cont

print(f'A soma de todos os {contNumeros} valores solictados é {soma}')