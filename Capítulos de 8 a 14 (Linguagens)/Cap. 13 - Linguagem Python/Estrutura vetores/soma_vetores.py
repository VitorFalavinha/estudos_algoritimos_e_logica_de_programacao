N = int(input('Quantos valores voce vai digitar? '))

vetA:[int] = [0 for x in range (N)]
vetB:[int] = [0 for x in range (N)]
vetC:[int] = [0 for x in range (N)]

print('Digite os valores do vetor A: ')
for i in range (N):
    vetA[i] = int(input())

print('Digite os valores do vetor B: ')
for i in range (N):
    vetB[i] = int(input())

print('VETOR RESULTANTE: ')
for i in range(N):
    vetC[i] = vetA[i] + vetB[i]
    print(vetC[i])

