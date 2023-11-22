n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

if n2 < n1: 
    menor = n2
elif n3 < n2:
    menor = n3 
else:
    menor = n1

print(f"MENOR = {menor}")