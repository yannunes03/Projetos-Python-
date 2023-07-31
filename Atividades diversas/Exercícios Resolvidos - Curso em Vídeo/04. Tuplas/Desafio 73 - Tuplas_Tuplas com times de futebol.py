'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
, na ordem de colocação. Depois mostre:'''

# Apenas os 5 primeiros colocados.
# Os últimos 4 colocados da tabela.
# Uma lista com os times em ordem alfabética.
# Em que posição na tabela está o time da 'Chapecoense'

tabela = ('Fluminense', 'Botafogo', 'Fortaleza', 'Palmeiras', 'Vasco', 'Internacional', 'Bragantino', 'Flamengo'
          , 'São Paulo', 'Goiás', 'Athetico-PR', 'Cruzeiro', 'Grêmio', 'Grêmio', 'Corinthians', 'Cuiabá'
          , 'Atlético-MG', 'Santos', 'Bahia', 'Coritiba', 'América-MG')

print(f'Os 5 primeiros colocados da tabela são: {tabela[0:5]}')
print(f'Os 4 últimos colocados da tabela são: {tabela[-4:]}')
print(f'Os times em ordem alfabética fica na seguinte forma {sorted(tabela)}')
time = str(input('Digite o nome do seu time para lhe revelarmos a posição dele na tabela'))
print(f'O seu time está na {tabela.index(time)+1} ª posição')