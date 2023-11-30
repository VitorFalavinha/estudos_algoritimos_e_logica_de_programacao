N = int(input('Qual a ordem da matriz? '))

mat = [[0 for x in range(N)]for x in range(N)]

for i in range(N):
    for j in range(N):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))
soma = 0
for i in range(N):
    for j in range(N):
        if mat[i][j] > 0:
            soma = soma + mat[i][j]
print()
print(f'SOMA DOS POSITIVOS = {soma:.1f}')

print()
l = int(input('Escolha uma linha: '))
print('LINHA ESCOLHIDA = ', end='')
for i in range(N):
    print(f'{mat[l][i]:.1f} ', end='')

print()
print()
c = int(input('Escolha uma coluna: '))
print('COLUNA ESCOLHIDA = ', end='')
for i in range(N):
    print(f'{mat[i][c]:.1f} ', end='')

print()
print()
print('DIAGONAL PRINCIPAL = ', end='')
for i in range(N):
    print(f'{mat[i][i]:.1f} ', end='')

for i in range(N):
    for j in range(N):
        if mat[i][j] < 0:
            mat[i][j] = (mat[i][j] ** 2)

print()
print()
print('MATRIZ ALTERADA: ')
for i in range(N):
    for j in range(N):
        print(f'{mat[i][j]:.1f} ', end='')
    print()