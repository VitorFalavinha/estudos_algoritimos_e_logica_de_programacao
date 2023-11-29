N = int(input('Quantos elementos terá o vetor? '))

number:[int] = [0 for x in range(N)]

for i in range(N):
    number[i] = int(input('Digite um numero: '))

qPares = 0 
somaPares = 0
for i in range(N):
    if number[i] % 2 == 0:
        qPares = qPares + 1
        somaPares = somaPares + number[i]

if qPares > 0:
    mediaPares = somaPares / qPares
    print(f'MEDIA DOS NUMEROS PARES = {mediaPares:.1f}')
else:
    print('NENHUM NUMERO PAR.')