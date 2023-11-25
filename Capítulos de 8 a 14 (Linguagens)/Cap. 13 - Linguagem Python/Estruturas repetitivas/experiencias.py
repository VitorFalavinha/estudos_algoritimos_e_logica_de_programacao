N: int; quantCob: int; totalCob: int; 
typeCob: str; 
rab: int; totalRab: int; percRab: float
rat: int; totalRat: int; percRat: float
frog: int; totalFrog: int; percFrog: float

N = int(input('Quantos casos de teste serao digitados? '))

totalCob = 0
totalRab = 0
totalRat = 0
totalFrog = 0

for i in range(0, N):
    quantCob = int(input('Quantidade de cobaias: '))
    typeCob = str(input('Tipo de cobaia: '))

    if typeCob == 'C' or typeCob == 'c':
        totalRab = totalRab + quantCob
    elif typeCob == 'R' or typeCob == 'r':
        totalRat = totalRat + quantCob
    elif typeCob == 'S' or typeCob == 's':
        totalFrog = totalFrog + quantCob

totalCob = totalRab + totalRat + totalFrog 

percRab = (totalRab * 100) / totalCob
percRat = (totalRat * 100) / totalCob
percFrog = (totalFrog * 100) / totalCob

print('\n')
print('RELATORIO FINAL: ')
print(f'TOTAL DE COBAIAS: {totalCob}')
print(f'TOTAL DE COELHOS: {totalRab}')
print(f'TOTAL DE RATOS: {totalRat}')
print(f'TOTAL DE SAPOS: {totalFrog}\n')
print(f'PERCENTUAL DE COELHOS: {percRab:.2f}')
print(f'PERCENTUAL DE RATOS: {percRat:.2f}')
print(f'PERCENTUAL DE SAPOS: {percFrog:.2f}')


    