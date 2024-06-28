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
    matrix_labels = [chr(ord('A') + i) for i in range(len(matrices))]  # Rotular matrizes com letras A, B, C, etc.
    while True:
        print("\nMatrizes disponíveis:")
        for label, matrix in zip(matrix_labels, matrices):
            print(f"Matriz {label}:")
            print(matrix)

        use_all_matrices = input("\nDeseja realizar os cálculos com TODAS as matrizes? (sim/não) ")

        if use_all_matrices.lower() == 'sim':
            # Verifica se todas as matrizes têm as mesmas dimensões
            if all(matrix.shape == matrices[0].shape for matrix in matrices):
                operation = input("Qual operação deseja realizar (soma, subtração, multiplicação)? ")

                if operation.lower() == 'soma':
                    result = sum(matrices)
                    print("Resultado da operação de soma:")
                    print(result)

                elif operation.lower() == 'subtração':
                    result = matrices[0]
                    for matrix in matrices[1:]:
                        result -= matrix
                    print("Resultado da operação de subtração:")
                    print(result)

                elif operation.lower() == 'multiplicação':
                    result = matrices[0]
                    for matrix in matrices[1:]:
                        if result.shape[1] == matrix.shape[0]:
                            result = np.matmul(result, matrix)
                        else:
                            print(f"As matrizes {matrix_labels[matrices.index(result)]} e {matrix_labels[matrices.index(matrix)]} não podem ser multiplicadas.")
                            break
                    print("Resultado da operação de multiplicação:")
                    print(result)

                else:
                    print("Operação não suportada.")

            else:
                print("As matrizes têm dimensões diferentes e não podem ser operadas juntas.")

        else:
            # Permite escolher matrizes e ordens específicas para realizar os cálculos
            operations = input("\nDigite as operações desejadas com as matrizes (exemplo: 'A + B', 'C * D', etc.): ")
            operations = operations.split(',')

            for op in operations:
                # Processar cada operação solicitada
                op = op.strip()
                elements = op.split()

                if len(elements) == 3:
                    matrix1_label = elements[0].upper()
                    operator = elements[1]
                    matrix2_label = elements[2].upper()

                    # Encontrar matrizes correspondentes aos rótulos
                    matrix1 = matrices[matrix_labels.index(matrix1_label)]
                    matrix2 = matrices[matrix_labels.index(matrix2_label)]

                    if operator == '+':
                        if matrix1.shape == matrix2.shape:
                            result = matrix1 + matrix2
                            print(f"Resultado de {matrix1_label} + {matrix2_label}:")
                            print(result)
                        else:
                            print(f"As matrizes {matrix1_label} e {matrix2_label} têm dimensões diferentes.")

                    elif operator == '-':
                        if matrix1.shape == matrix2.shape:
                            result = matrix1 - matrix2
                            print(f"Resultado de {matrix1_label} - {matrix2_label}:")
                            print(result)
                        else:
                            print(f"As matrizes {matrix1_label} e {matrix2_label} têm dimensões diferentes.")

                    elif operator == '*':
                        if matrix1.shape[1] == matrix2.shape[0]:
                            result = np.matmul(matrix1, matrix2)
                            print(f"Resultado de {matrix1_label} * {matrix2_label}:")
                            print(result)
                        else:
                            print(f"As matrizes {matrix1_label} e {matrix2_label} não podem ser multiplicadas.")

                    else:
                        print(f"Operação não suportada: {op}")

                else:
                    print(f"Entrada inválida: {op}")

        another_operation = input("\nDeseja efetuar outro cálculo com as matrizes encontradas? (sim/não) ")
        if another_operation.lower() != 'sim':
            print("Obrigado, volte sempre!")
            break

def main():
    matrices = []
    matrix_labels = []

    while True:
        matrices.append(create_matrix())
        another = input("Deseja criar outra matriz (sim/não)? ")
        if another.lower() != "sim":
            break

    if matrices:
        operations = input("\nDeseja realizar operações com as matrizes criadas (sim/não)? ")
        if operations.lower() == 'sim':
            matrix_operations(matrices)

main()