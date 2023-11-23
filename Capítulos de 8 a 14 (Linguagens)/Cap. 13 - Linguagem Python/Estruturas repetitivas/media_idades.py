age: int; add: int; avrg: float; count: int

print('Digite as idades:')
age = int(input())

if age < 0:
    print('IMPOSSÍVEL CALCULAR. ')
else:
    add = 0
    count = 0
    while age >= 0:
        add = add + age
        count = count + 1
        age = int(input(''))

    avrg = add / count

    print(f'MEDIA = {avrg:.2f}')


