x = float(input('Valor de X: '))
y = float(input('Valor de Y: '))

if x > 0 and y > 0:
    print('Quadrante Q1.')
elif x < 0 and y > 0:
    print('Quadrante Q2.')
elif x < 0 and y < 0:
    print('Quadrante Q3.')
elif x > 0 and y < 0:
    print('Quadrante Q4')
elif x == 0 and y == 0:
    print('Origem.')
elif x == 0 and y != 0:
    print('Eixo Y.')
elif x != 0 and y == 0:
    print('Eixo X.')