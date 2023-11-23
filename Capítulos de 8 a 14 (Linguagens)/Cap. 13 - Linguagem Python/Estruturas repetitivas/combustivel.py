code = int(input('Informe um codigo (1, 2, 3) ou 4 para parar:'))
alc = 0
gas = 0
die = 0
while code != 4:
   
    if code == 1:
        alc = alc + 1
    elif code == 2:
        gas = gas + 1
    elif code == 3:
        die = die + 1
    
    code = int(input('Informe um codigo (1, 2, 3) ou 4 para parar:'))

print(f'Alcool: {alc}')
print(f'Gasolina: {gas}')
print(f'Diesel: {die}')