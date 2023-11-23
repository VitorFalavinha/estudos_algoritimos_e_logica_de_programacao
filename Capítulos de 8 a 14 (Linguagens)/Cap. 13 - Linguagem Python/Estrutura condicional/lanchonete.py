code = int(input('Código do produto: '))
quant = int(input('Quantidade comprada: '))

match code:
    case 1: 
        pay = quant * 5.00
    case 2:
        pay = quant * 3.50
    case 3: 
        pay = quant * 4.80
    case 4: 
        pay = quant * 8.90
    case 5: 
        pay = quant * 7.32

print(f'Valor a pagar: R$ {pay:.2f}')
