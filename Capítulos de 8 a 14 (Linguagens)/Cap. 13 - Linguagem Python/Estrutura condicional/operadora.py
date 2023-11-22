min: int
minOver: int
pay: float

min = int(input("Digite a quantidade de minutos: "))

if min > 100: 
    minOver = min - 100
    pay = minOver * 2.0 + 50.0
    print(f"Valor a pagar: R$ {pay:.2f}")
else:
    print("Valor a pagar: R$ 50,00")
