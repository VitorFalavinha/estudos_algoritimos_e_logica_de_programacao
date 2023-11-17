a = float(input("Digite a medida A: "))
b = float(input("Digite a medida B: "))
c = float(input("Digite a medida C: "))

areaSquare = a ** 2
areaTriangle = a * b / 2
areaTrapezio = ((a + b) * c) / 2

print(f"AREA DO QUADRADO = {areaSquare:.4f}")
print(f"AREA DO TRIANGULO = {areaTriangle:.4f}")
print(f"AREA DO TRAPEZIO = {areaTrapezio:.4f}")