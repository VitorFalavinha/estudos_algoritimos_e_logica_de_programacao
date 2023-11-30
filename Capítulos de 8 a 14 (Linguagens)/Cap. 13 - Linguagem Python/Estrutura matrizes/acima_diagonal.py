N = int(input('Qual a ordem da matriz? '))

mat = [[0 for x in range(N)] for x in range(N)]

for i in range(N):
    for j in range(N):
        mat[i][j] = int(input(f'Elemento: [{i},{j}]'))

soma = 0
for i in range(N):
    for j in range(i+1, N):
        soma = soma + mat[i][j]

print('SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = ',soma)