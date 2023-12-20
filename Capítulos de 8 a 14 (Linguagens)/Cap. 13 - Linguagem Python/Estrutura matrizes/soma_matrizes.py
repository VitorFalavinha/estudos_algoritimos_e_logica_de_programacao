M = int(input('Quantas linhas terá sua matriz? '))
N = int(input('Quantas colunas tera sua matriz? '))

A = [[0 for x in range(N)]for x in range(M)]
B = [[0 for x in range(N)]for x in range(M)]
C = [[0 for x in range(N)]for x in range(M)]

print('Digite os valores da matriz A: ')
for i in range(M):
    for j in range(N):
        A[i][j] = int(input(f'Elemento [{i},{j}]: '))

print('Digite os valores da matriz B: ')
for i in range(M):
    for j in range(N):
        B[i][j] = int(input(f'Elemento [{i},{j}]: '))

print('MATRIZ SOMADA: ')
for i in range(M):
    for j in range(N):
        C[i][j] = A[i][j] + B[i][j]
        print(f'{C[i][j]} ', end='')
    print()