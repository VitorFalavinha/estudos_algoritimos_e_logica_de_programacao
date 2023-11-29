N = int(input('Quantos numeros voce vai digitar? '))

number:[float] = [0 for x in range(N)]

for i in range(N):
    number[i] = float(input('Digite um numero: '))

maior = number[0]
for i in range(1,N):
    if number[i] > maior:
        maior = number[i]
        posicao = i
print()
print(f'MAIOR VALOR = {maior:.1f}')
print('POSIÇÃO DO MAIOR VALOR = ', posicao)