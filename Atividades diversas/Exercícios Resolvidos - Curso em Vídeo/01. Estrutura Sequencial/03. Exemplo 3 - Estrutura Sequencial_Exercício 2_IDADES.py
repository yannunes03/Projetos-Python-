nome1: str ; nome2: str ; DadosPessoa1: str ; DadosPessoa2: str
idade1: int ; idade2: int ; media: int

nome1 = input('Nome da Pessoa 1: ')
idade1 = input('Idade Pessoa 1: ')
DadosPessoa1 = input('Dados Pessoa 1: ')
print()
nome2 = input('Nome da Pessoa 2: ')
idade2 = input('Idade Pessoa 2: ')
DadosPessoa2 = input('Dados Pessoa 2: ')

media = (int(idade1) + int(idade2)) / 2
print(f"A idade média de {nome1} e {nome2} é de {media:.3f} anos ")