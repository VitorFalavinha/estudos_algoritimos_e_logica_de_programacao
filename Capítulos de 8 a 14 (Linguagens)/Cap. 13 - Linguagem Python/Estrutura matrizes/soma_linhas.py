M = int(input('Qual a quantidade de linhas da matriz? '))
N = int(input('Qual a quantidade colunas da matriz? '))

mat = [[0 for x in range(N)] for x in range(M)]
vet = [0 for x in range(M)]

for i in range(M):
    print(f'Digite os elementos da {i+1}ª linha:')
    for j in range(N):
        mat[i][j] = int(input(''))

print('VETOR GERADO: ')
for i in range(M):
    for j in range(N):
        vet[i] = vet[i] + mat[i][j]

for i in range(M):
    print(f'{vet[i]:.1f}')


