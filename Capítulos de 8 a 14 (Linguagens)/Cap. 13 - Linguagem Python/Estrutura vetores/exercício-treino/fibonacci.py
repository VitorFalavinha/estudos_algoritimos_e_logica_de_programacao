t1: int; t2: int; t3:int; cont:int

N = int(input('Quantos termos da sequência de Fibonacci vamos mostrar? '))

t1 = 0
t2 = 1
t3 = t1 + t2
cont = 2
print(t1,'-', t2, end=' - ')

def repeat(t1, t2, t3, cont):
    if cont < N:
        t3 = t1 + t2
        print(t3, end=' - ')
        t1 = t2
        t2 = t3
        cont = cont+1
        repeat(t1, t2, t3, cont)
    else:
        print('Fim!')


repeat(t1, t2, t3, cont)

#for i in range(3,N+1):
#    t3 = t1 + t2
#    print(t3, end=' - ')
#    t1 = t2
#    t2 = t3
#    if i == N:
#        print('FIM!')

