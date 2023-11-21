n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

nFinal = n1 + n2

print(f"NOTA FINAL = {nFinal:.1f}")

if nFinal < 60.0:
    print("REPROVADO")