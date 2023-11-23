salary: float; newSalary: float; plus: float; percent: int 

salary = float(input('Digite o salário da pessoa: '))

if salary <= 1000:
   plus = salary * 0.2
   percent = 20
elif salary <= 3000:
    plus = salary * 0.15
    percent = 15
elif salary <= 8000:
    plus = salary * 0.1
    percent = 10
else:
    plus = salary * 0.05
    percent = 5

newSalary = salary + plus

print(f'Novo salário: R$ {newSalary:.2f}')
print(f'Aumento: R$ {plus:.2f}')
print(f'Porcentagem: {percent}%')
