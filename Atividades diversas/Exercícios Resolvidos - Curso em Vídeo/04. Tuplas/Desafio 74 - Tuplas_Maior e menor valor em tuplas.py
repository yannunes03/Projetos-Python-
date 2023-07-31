'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
que estão na tupla'''
import random
from random import  randint

lista = (random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100))

print(f'A lista de números gerados é {lista}')
print(f'O menor número dessa lista é {min(lista)}')
print(f'O maior número dessa lista é {max(lista)}')
print(f'A disposição dessa lista de forma ordenada, fica da seguinte forma {sorted(lista)}')
