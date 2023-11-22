
print("Digite as três distâncias:")
n1 = float(input())
n2 = float(input())
n3 = float(input())

if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n2 and n3 > n1:
    maior = n3
else:
    maior = n1

print(f"MAIOR DISTANCIA = {maior:.2f}")