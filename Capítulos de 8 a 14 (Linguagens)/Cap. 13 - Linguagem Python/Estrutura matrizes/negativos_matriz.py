M = int(input('Quantidade de linhas da matriz: '))
N = int(input('Quanidade de colunas da matriz: '))

mat = [[0 for x in range(N)] for x in range(M)]

for i in range(M):
    for j in range(N):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))
    
print('VALORES NEGATIVOS: ')
for i in range(M):
    for j in range(N):
        if mat[i][j] < 0:
            print(mat[i][j])