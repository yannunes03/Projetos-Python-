'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e
mostre uma mensagem com tamanho adaptável'''



def escreva():
    tamanho = len(texto)
    print((4 + tamanho) * '~')
    print(f'  {texto}')
    print((4 + tamanho) * '~')

texto = str(input('Informe o testo a ser verificado: '))
escreva()


