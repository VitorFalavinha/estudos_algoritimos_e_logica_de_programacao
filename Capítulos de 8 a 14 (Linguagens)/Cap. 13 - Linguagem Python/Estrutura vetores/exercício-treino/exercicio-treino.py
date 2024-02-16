N = int(input('Numero de pessoas cadastradas: '))

height:[float] = [0 for x in range(N)]
gender:[str]=[0 for x in range(N)]

somaHeight = 0
genderMale = 0
genderFem = 0
for i in range (N):
    height[i] = float(input(f'Altura da {i+1}ª pessoa: '))
    gender[i] = str(input(f'Gênero da {i+1}ª pessoa: '))
    somaHeight = somaHeight + height[i]

    if gender[i] == 'M':
        genderMale = genderMale + 1
    else:
        genderFem = genderFem + 1 

mediaHeight = somaHeight/N 

print(f'A média das alturas das pessoas digitadas é: {mediaHeight:.2f}')
print(f'Foram digitados os dados de {genderFem} mulheres e {genderMale} homens.')
    
