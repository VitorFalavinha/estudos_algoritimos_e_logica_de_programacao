M = int(input('Quantas linhas terá a matriz? '))
N = int(input('Quantas colunas terá a matriz? '))

mat:[int] = [[0 for x in range(N)] for x in range(M)]

for i in range(M):
    for j in range(N):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))

print()
print('MATRIZ DIGITADA: ')
for i in range(M):
    for j in range(N):
        print(f'{mat[i][j]} ', end='')
    print()
