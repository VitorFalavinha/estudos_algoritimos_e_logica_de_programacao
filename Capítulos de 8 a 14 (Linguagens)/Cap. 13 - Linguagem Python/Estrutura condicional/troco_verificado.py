unitPrice: float
quant: int
cash: float
change: float

unitPrice = float(input("Preço unitário do produto: "))
quant = int(input("Quantidade comprada: "))
cash = float(input("Dinheiro recebido: "))



if cash > unitPrice * quant:
    change = cash - unitPrice * quant
    print(f"TROCO = R$ {change:.2f}")
else:
    change = unitPrice * quant - cash
    print(f"DINHEIRO INSUFICIENTE. FALTAM {change:.2f} REAIS. ")