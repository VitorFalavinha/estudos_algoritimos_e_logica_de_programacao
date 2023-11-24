n: int; add: int

n = int(input('Digite um numero inteiro: '))

while n != 0:
    if n % 2 != 0:
        n = n + 1
    
    add = 5 * n + 20        
    print(add)        
    n = int(input('Digite um numero inteiro: '))