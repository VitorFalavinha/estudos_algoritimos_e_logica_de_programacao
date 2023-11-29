N = int(input('Quantos elementos voce vai digitar? '))

number:[float] = [0 for x in range (N)]

for i in range (N):
    number[i] = float(input('Digite um numero: '))

somaVet = 0
for i in range(N):
    somaVet = somaVet + number[i]

mediaVet = somaVet / N
print()
print(f'MEDIA DO VETOR = {mediaVet:.3f}')
print('ELEMENTOS ABAIXO DA MEDIA: ')

for i in range (N):
    if number[i] < mediaVet:
        print(number[i])
    