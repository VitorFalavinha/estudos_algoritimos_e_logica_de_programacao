print('Digite os valores das coodernadas X e Y: ')
x = int(input(''))
y = int(input(''))

while x != 0 and y != 0:
    if x > 0 and y > 0:
        print('Quadrante Q1')
    elif x < 0 and y > 0:
        print('Quadrante Q2')
    elif x < 0 and y < 0: 
        print('Quadrante Q3')
    else:
        print('Quadrante Q4')

    print('Digite os valores das coodernadas X e Y: ')
    x = int(input(''))
    y = int(input(''))