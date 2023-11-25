N: int; n: int; inside: int; outside: int

N = int(input('Quantos numeros voce vai digitar? '))

inside = 0
outside = 0
for i in range(0, N):
    n = int(input('Digite um numero: '))
    if n < 10 or n > 20:
        outside = outside + 1
    else:
        inside = inside + 1

print(f'{inside} DENTRO')
print(f'{outside} FORA')