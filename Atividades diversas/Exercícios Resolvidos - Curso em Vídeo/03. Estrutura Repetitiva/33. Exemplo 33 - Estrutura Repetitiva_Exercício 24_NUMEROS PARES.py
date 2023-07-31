'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50'''

from time import sleep

for contadorPares in range(1,51):

    if contadorPares % 2 == 0:
        print(contadorPares)
    sleep(0.5)
