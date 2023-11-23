print('Digite dois numeros inteiros:')
n1 = int(input(''))
n2 = int(input(''))

if n1 % n2 == 0 or n2 % n1 == 0: 
    print('São múltiplos.')
else:
    print('Não são múltiplos.')
