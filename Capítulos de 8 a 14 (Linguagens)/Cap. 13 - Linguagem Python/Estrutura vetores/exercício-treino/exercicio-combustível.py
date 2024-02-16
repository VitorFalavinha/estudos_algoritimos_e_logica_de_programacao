tripN: int
kmL: float
triplenght: float
tripTotalLenght: float
priceLitter: float

def repetirCalculo(repeat):
    triplenght = float(input('Digite a distância até o local: ')) 
    kmL = float(input('Quilômetros por litro: '))
    priceLitter = float(input('Valor do litro: '))
    tripN = int(input('Número de viagens: '))

    tripTotalLenght = (triplenght*2) * tripN #Considerando ida e volta

    print(f'O valor final do consumo pelas viagens é: R${(tripTotalLenght/kmL)*priceLitter:.2f}')

    repeat = (input('Deseja adicionar outro local? (S/N)'))
    if repeat == 'S' or 's':
        repetirCalculo(repeat)
    else:
        print('Obrigado pela sua participação!')


repetirCalculo(repetirCalculo)



