N = int(input('Quantos numeros voce vai digitar? '))

vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input('Digite um numero: '))

soma = 0
print('VALORES: ', end='')
for i in range(0, N):
    soma = soma + vet[i]
    print(f' {vet[i]:.1f} ', end='') 

media = soma / N
print()
print(f'SOMA = {soma:.1f}')
print(f'MEDIA = {media:.1f}')