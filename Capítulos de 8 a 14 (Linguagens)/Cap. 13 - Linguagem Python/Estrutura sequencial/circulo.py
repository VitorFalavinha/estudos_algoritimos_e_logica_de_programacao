radius = float(input("Digite o valor do raio do círculo: "))

while radius <= 0:
    print("Valor inválido!")
    radius = float(input("Digite o valor do raio do círculo: "))

area = 3.14 * (radius**2)

print(f"AREA = {area:.3f}")