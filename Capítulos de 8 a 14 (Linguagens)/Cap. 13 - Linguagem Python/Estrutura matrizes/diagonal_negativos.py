N = int(input('Qual a ordem da matriz? '))

mat = [[0 for x in range(N)] for x in range(N)]

for i in range(N):
    for j in range(N):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))

print('DIAGONAL PRINCIPAL: ')

for i in range(N):
    for j in range(N):
        if [i] == [j]:
            print(f'{mat[i][j]} ', end='')

quantNeg = 0
for i in range(N):
    for j in range(N):
        if mat[i][j] < 0:
            quantNeg = quantNeg + 1
print()
print('QUANTIDADE DE NEGATIVOS = ', quantNeg)

