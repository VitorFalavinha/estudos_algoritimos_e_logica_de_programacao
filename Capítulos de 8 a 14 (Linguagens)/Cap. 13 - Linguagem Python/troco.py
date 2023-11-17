unitPrice: float
quant: int
pay: float
change: float

unitPrice = float(input("Preço unitario do produto: "))
quant = int(input("Quantidade comprada: "))
pay = float(input("Dinheiro recebido: "))

change = pay - (unitPrice * quant)

print(f"TROCO = {change:.2f}")
