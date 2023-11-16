base: float
height: float
area: float
perimeter: float
diagonal: float

base = float(input("Base do retangulo:"))
height = float(input('Altura do retangulo:'))

area = base * height
perimeter = (base + height) * 2
diagonal = (height ** 2 + base ** 2 ) ** 0.5

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimeter:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")
