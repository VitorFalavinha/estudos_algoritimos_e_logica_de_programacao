width: float
lenght: float
SquarePrice: float
area: float
finalPrice: float

width = float(input("Digite a largura do terreno:"))
lenght = float(input("Digite o comprimento do terreno:"))
SquarePrice = float(input("Digite o valor do metro quadrado:"))

area = width * lenght
finalPrice = area * SquarePrice

print(f"Area do terreno = {area:.2f}")
print(f"Preco do terreno =  {finalPrice:.2f}")