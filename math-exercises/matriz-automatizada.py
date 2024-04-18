import numpy as np

def create_matrix():
    rows = int(input("Digite o número de linhas da matriz: "))
    cols = int(input("Digite o número de colunas da matriz: "))
    law = input("Digite a lei de formação da matriz. Exemplo: para aij = i+j, digite 'i+j': ")
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            # Avalia a lei de formação como uma expressão matemática
            matrix[i][j] = eval(law.replace("i", str(i+1)).replace("j", str(j+1)))
    print("Matriz criada: ")
    print(matrix)
    return matrix

def matrix_operations(matrices):
    operation = input("Qual operação deseja realizar (soma, subtração)? ")
    if operation.lower() == "soma" or operation.lower() == "subtração":
        # Verifica se todas as matrizes têm as mesmas dimensões
        if all(matrix.shape == matrices[0].shape for matrix in matrices):
            if operation.lower() == "soma":
                result = sum(matrices)  # Soma válida de matrizes
            else:
                result = matrices[0]
                for matrix in matrices[1:]:
                    result -= matrix
            print("Resultado da operação: ")
            print(result)
        else:
            print(f"Impossível realizar a operação: as matrizes têm dimensões diferentes.")
    else:
        print("Operação não suportada.")

def main():
    matrices = []
    while True:
        matrices.append(create_matrix())
        another = input("Deseja criar outra matriz (sim/não)? ")
        if another.lower() != "sim":
            break
    if matrices:
        operation = input("Deseja realizar operações com as matrizes criadas (sim/não)? ")
        if operation.lower() == "sim":
            matrix_operations(matrices)

main()

