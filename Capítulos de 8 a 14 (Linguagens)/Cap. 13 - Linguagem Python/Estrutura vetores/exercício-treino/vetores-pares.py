N = int(input('Quantos numeros voce vai digitar?'))

vet:[int] = [0 for x in range (N)]

for i in range(N):
    vet[i] = int(input('Digite um numero: '))

nPairs = 0
print('Numeros pares digitados: ')

for i in range(N):
    if vet[i] % 2 == 0:
        print(vet[i], end=' ')
        nPairs = nPairs + 1

print()
print(f'Quantidade de numeros pares: {nPairs}')
