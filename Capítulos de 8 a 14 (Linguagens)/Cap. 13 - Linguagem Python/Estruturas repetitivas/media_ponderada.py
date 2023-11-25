N: int; n1: float; n2: float; n3: float; add: float; avg: float

N = int(input('Quantos casos voce vai digitar? '))

for i in range(0, N):
    print('Digite tres numeros: ')
    n1 = float(input(''))
    n2 = float(input(''))
    n3 = float(input(''))

    avg = (n1 * 0.2) + (n2 * 0.3) + (n3 * 0.5)
    print(f'MEDIA = {avg:.1f}')
    