NCasos: int ; NCobaias: int ; Coelhos: int ; Ratos: int ; Sapos: int
TCobaias: str
PCoelhos: float ; PRatos: float ; PSapos: float

NCasos = int(input('Quantos casos de teste serao digitados? '))

for i in range (0, NCasos):
    NCobaias = int(input('Quantidade de cobaias: '))
    TCobaias = int(input(('Tipo de Cobaia: ')))
    if TCobaias =='C':
        coelhos = Coelhos + NCobaias
    elif TCobaias == 'R':
        Ratos = Ratos + NCobaias
    elif TCobaias == 'S':
        Sapos = Sapos + NCobaias

print('RELATÓRIO FINAL: ')
print('Total de Cobaias: ', Coelhos + Ratos + Sapos)
print('Total de Coelhos: ', Coelhos)
print('Total de Ratos: ', Ratos)
print('Total de Sapos: ', Sapos)

PCoelhos = (Coelhos / (Coelhos + Ratos + Sapos))*100
PRatos = (Ratos / (Coelhos + Ratos + Sapos))*100
PSapos = (Sapos / (Coelhos + Ratos + Sapos))*100

print('Percentual de Coelhos: {:.2f}'.format(PCoelhos))
print('Percentual de Ratos: {:.2f}'.format(PRatos))
print('Percentual de Sapos: {:.2f}'.format(PSapos))

