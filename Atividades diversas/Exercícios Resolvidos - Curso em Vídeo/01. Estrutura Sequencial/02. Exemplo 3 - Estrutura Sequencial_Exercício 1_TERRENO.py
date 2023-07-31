'''
Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
casal decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
duas casas decimais
'''

largura: float
comprimento: float
metroQuadrado: float
area: float
preco: float

largura = float(input("Digite a Largura do terreno: "))
print()
comprimento = float(input("Digite o comprimento do terreno: "))
print()
metroQuadrado = float(input("Digite o valor do metro quadrado: R$ "))
print()
print("Logo")
print()

area = largura * comprimento
preco = area * metroQuadrado

print(f"Área do tereno = {area:.2f}")
print(f"Preço do terreno = {preco:.2f}")

