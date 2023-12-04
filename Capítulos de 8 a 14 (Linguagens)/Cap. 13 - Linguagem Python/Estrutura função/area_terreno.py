def areaTerreno():
    area = a * b
    print(f'A área de um terreno {a} X {b} é de {area}m².')

print('Controle de terrenos: ')
print('-' * 30)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
areaTerreno()