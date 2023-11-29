N: int; qPairs: int

N = int(input('Quantos numeros voce vai digitar? '))

number:[int] = [0 for x in range(N)]

for i in range (N):
    number[i] = int(input('Digite um numero: '))

qPairs = 0
print('NUMEROS PARES: ')
for i in range(N):
    if number[i] % 2 == 0:
        qPairs = qPairs + 1
        print(number[i],'  ', end='')

print()
print(f'QUANTIDADE DE PARES: {qPairs}')


