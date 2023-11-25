N: int; fat: int

N = int(input('Digite o valor de N: '))

fat = 1
for i in range(N,0,-1):
    fat = fat * i

print('FATORIAL = ', fat)