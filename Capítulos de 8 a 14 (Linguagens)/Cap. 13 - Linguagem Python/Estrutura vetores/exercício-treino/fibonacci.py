t1: int; t2: int; t3:int; cont:int

N = int(input('Quantos termos da sequência de Fibonacci vamos mostrar? '))

t1 = 0
t2 = 1
cont = 2
print(t1,'-', t2, end=' - ')

def repeat(t3):
    while cont < N:
        t3 = t1 + t2
        print(t3)
        t1 = t2
        t2 = t3
        cont = cont+1
        repeat(t3)


repeat(repeat)

#for i in range(3,N+1):
#    t3 = t1 + t2
#    print(t3, end=' - ')
#    t1 = t2
#    t2 = t3
#    if i == N:
#        print('FIM!')

