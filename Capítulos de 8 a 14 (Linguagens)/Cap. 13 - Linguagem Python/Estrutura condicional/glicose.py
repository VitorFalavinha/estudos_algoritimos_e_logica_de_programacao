glicose: float

glicose = float(input("Digite a medida de glicose: "))

print("Classificação: ", end="")

if glicose <= 100:
    print("normal")
elif glicose <= 140:
    print("elevado")
else:
    print("diabetes")