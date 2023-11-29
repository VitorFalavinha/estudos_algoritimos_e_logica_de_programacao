N = int(input('Quantos alunos serão digitados? '))

name:[str] = [0 for x in range(N)]
n1:[float] = [0 for x in range(N)]
n2:[float] = [0 for x in range(N)]

for i in range(N):
    print(f'Digite nome, primeira e segunda nota do {i+1}o aluno:')
    name[i] = str(input('')) 
    n1[i] = float(input(''))
    n2[i] = float(input(''))
print()
print('ALUNOS APROVADOS:')
for i in range(N):
    if (n1[i] + n2[i]) / 2 >= 6:
        print(name[i])



