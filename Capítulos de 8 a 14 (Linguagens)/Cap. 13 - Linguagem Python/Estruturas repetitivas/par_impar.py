N: int; n: int

N = int(input('Quantos numeros voce vai digitar? '))

for i in range(0,N):
    n = int(input('Digite um numero: '))
    if n % 2 == 0 and n > 0:
        print('PAR POSITIVO')
    elif n % 2 == 0 and n < 0: 
        print('PAR NEGATIVO')
    elif n % 2 != 0 and n > 0:
        print('IMPAR POSITIVO')
    elif n % 2 != 0 and n < 0:
        print('IMPAR NEGATIVO')
    else:
        print('NULO')