'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
o nome do jogador e quantas partidas ele jogo. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato'''

dados = {}
soma = 0

dados['nome'] = str(input('Nome do Jogador: '))
dados['partidas'] = int(input(f"Quantas partidas {dados['nome']} jogou? "))
dados['gols'] = list()

for n in range(0,dados['partidas']):
     dados['gols'].append(int(input(f"    Quantos gols na {n + 1}ª partida? ")))

print('-=' * 30)
print(dados)
print('-=' * 30)

for k,v in dados.items():
     print(f"O campo {k} tem valor {v}")

print('-=' * 30)
print(f"O jogador {dados['nome']} jogou {dados['partidas']} partidas")

for o in range(0, dados['partidas']):
     print(f"   => Na {o + 1}ª partida, fez {dados['gols'][o]} gols")
print(f"foi um total de {sum(dados['gols'])} gols.")
