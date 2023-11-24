n1: int; n2: int; nC: int; add: int

print('Digite dois numeros: ')
n1 = int(input(''))
n2 = int(input(''))

if n1 > n2:
    nC = n1
    n1 = n2
    n2 = nC

add = 0
for i in range(n1+1, n2):
    if i % 2 != 0:
            add = add + i

print(f'SOMA DOS IMPARES = {add}')