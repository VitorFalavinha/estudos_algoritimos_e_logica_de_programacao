N = int(input('Quantas pessoas voce vai digitar? '))

name:[str] = [0 for x in range(N)]
age:[int] = [0 for x in range (N)]

for i in range(N):
    print(f'Dados da {i + 1}ª pessoa: ')
    name[i] = str(input('Nome: '))
    age[i] = int(input('Idade: '))

oldest = age[0]
nameOldest = name[0]
for i in range(1,N):
    if age[i] > oldest:
        oldest = age[i]
        nameOldest = name[i]

    
print(f'PESSOA MAIS VELHA: {nameOldest}')