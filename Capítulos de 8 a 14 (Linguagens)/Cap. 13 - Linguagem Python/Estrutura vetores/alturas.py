N: int; menores: int; menoresPerc: float; somaAlt: float; mediaAlt: float

N = int(input('Quantas pessoas serão digitadas? '))

nome: [str] = [0 for x in range (N)]
idade: [int] = [0 for x in range (N)]
altura: [float] = [0 for x in range (N)]

for i in range (N):
    print(f'Digite os dados da {i+1}ª pessoa: ')
    nome[i] = str(input('Nome: '))
    idade[i] = int(input('Idade: '))
    altura[i] = float(input('Altura: '))

somaAlt = 0.0
for i in range(N):
    somaAlt = somaAlt + altura[i]

mediaAlt = somaAlt / N
print()
print(f'Altura média: {mediaAlt:.2f}')

menores = 0
for i in range (N):
    if idade[i] < 16:
        menores = menores + 1

menoresPerc = (menores / N) * 100
print(f'Pessoas menores de 16 anos: {menoresPerc:.1f}% e seus nomes são:')

for i in range(N):
    if idade[i] < 16:
        print(nome[i])