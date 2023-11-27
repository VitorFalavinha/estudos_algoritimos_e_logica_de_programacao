N: int

N = int(input('Quantos numeros voce vai digitar? '))
vet: [int] = [0 for x in range(N)]
for i in range(0, N):
    vet[i] = int(input('Digite um numero: '))

print()
print('NUMEROS NEGATIVOS: ')

for i in range(0, N):
    if vet[i] < 0:
        print(vet[i])