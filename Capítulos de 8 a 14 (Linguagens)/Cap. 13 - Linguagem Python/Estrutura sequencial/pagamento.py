name = str(input("Nome: "))
paymentPerHour = float(input("Valor por hora: "))
hoursWorked = float(input("Horas trabalhadas: "))

paymentTotal = paymentPerHour * hoursWorked

print(f"O pagamento para {name} será de R${paymentTotal:.2f}")