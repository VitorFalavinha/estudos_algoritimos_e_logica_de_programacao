N: int; name: str; age: int; youngest: int; oldest: int

N =  int(input('Quantos jogadores serão digitados? '))


for i in range(0, N):
    name = str(input(f'Nome do jogador {i+1}: '))
    age = int(input(f'Idade do jogador {i+1}: '))

    if i == 0:
        oldest = age
        nameOldest = name
        youngest = age
        nameYoungest = name

    if age > oldest:
        oldest = age
        nameOldest = name
    elif age < youngest:
        youngest = age 
        nameYoungest = name
        
print('\n')   
print(f'{nameOldest} é o jogador mais velho com {oldest} anos.')
print(f'{nameYoungest} é o jogador mais jovem com {youngest} anos.')
