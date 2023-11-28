N = int(input('Quantas pessoas serão digitadas? '))

name:[str] = [0 for x in range(N)]
age:[int] = [0 for x in range(N)]
height:[float] = [0 for x in range(N)]

for i in range(0,N):
    print(f'Dados da {i+1}ª pessoa: ')
    name = str(input('Nome: '))
    age = int(input('Idade: '))
    height = float(input('Altura: '))

addHeight = 
for i in range(0,N):
    addHeight = addHeight + height[i]

avgHeight = addHeight / N
print()
print(f'Altura média: {avgHeight:.2f}')

less16 = 0
for i in range(0,N):
    if age[i] < 16:
        less16 = less16 + 1
    
less16_per = (N / less16) * 100

print(f'Pessoas com menos de 16 anos: {less16_per:.}')

for i in range(0,N):
    if age[i] < 16:
        print(name[i])


