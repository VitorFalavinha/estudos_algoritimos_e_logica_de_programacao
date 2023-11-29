N = int(input('Quantas pessoas serão digitadas? '))

height:[float] = [0 for x in range(N)]
gender:[str] = [0 for x in range(N)]

for i in range(N):
    height[i] = float(input(f'Altura da {i+1}ª pessoa: '))
    gender[i] = str(input(f'Genero da {i+1}ª pessoa: '))

print()
menorAlt = height[0]
maiorAlt = height[0]
for i in range(1,N):
    if height[i] < menorAlt:
        menorAlt = height[i]
for i in range(1,N):
    if height[i] > maiorAlt:
        maiorAlt = height[i]

nWomen = 0  
somaHeight = 0      
for i in range(N):
    if gender[i] == 'f' or gender[i] == 'F':
        nWomen = nWomen + 1
        somaHeight = somaHeight + height[i]

mediaAlt = somaHeight / nWomen
nMen = N - nWomen
print(f'MENOR ALTURA = {menorAlt:.2f}')
print(f'MAIOR ALTURA = {maiorAlt:.2f}')
print(f'MEDIA DAS ALTURAS DAS MULHERES = {mediaAlt:.2f}')
print(f'NUMERO DE HOMENS = {nMen}')



