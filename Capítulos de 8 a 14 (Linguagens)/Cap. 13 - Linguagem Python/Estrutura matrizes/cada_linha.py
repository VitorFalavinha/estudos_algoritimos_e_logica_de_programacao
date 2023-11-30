N = int(input('Qual a ordem da matriz? '))

mat = [[0 for x in range(N)] for x in range(N)]

for i in range(N):
    for j in range(N):
        mat[i][j] = int(input(f'Elemento [{i},{j}]: '))

print()
print('MAIOR ELEMENTO DE CADA LINHA: ')
for i in range(N):
    maior = mat[i][0]
    for j in range(1,N):
        if mat[i][j] > maior:
            maior = mat[i][j]
    print(maior)
