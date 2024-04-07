import numpy as np


def display_matrix(matrix):
    for row in matrix:
        print(row)


def get_determinant(matrix):
    determinant = 0
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        for i in range(len(matrix)):
            multiplier = matrix[0][i]
            reduced_matrix = np.delete(np.delete(matrix, 0, 0), i, 1)
            if i % 2 == 0:
                determinant += multiplier * get_determinant(reduced_matrix)
            else:
                determinant -= multiplier * get_determinant(reduced_matrix)

    return determinant


def get_cofactors_matrix(matrix):
    cofactors_matrix = np.zeros((len(matrix), len(matrix)))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            multiplier = -1
            for k in range(i + j + 1):
                multiplier *= -1

            reduced_matrix = np.delete(np.delete(matrix, i, 0), j, 1)
            cofactor = multiplier * get_determinant(reduced_matrix)
            cofactors_matrix[i][j] = cofactor

    return cofactors_matrix


def get_adjoint_matrix(matrix):
    cofactors_matrix = get_cofactors_matrix(matrix)
    adjoint_matrix = np.transpose(cofactors_matrix)
    return adjoint_matrix


def get_inverse_matrix(matrix):
    inverse_matrix = np.zeros((len(matrix), len(matrix)))
    adjoint_matrix = get_adjoint_matrix(matrix)
    det = get_determinant(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            inverse_matrix[i][j] = adjoint_matrix[i][j] / det

    return inverse_matrix


def get_diagonal_matrix(matrix):
    diagonal_matrix = np.zeros((len(matrix), len(matrix)))
    for i in range(len(matrix)):
        diagonal_matrix[i][i] = matrix[i][i]

    return diagonal_matrix


def get_lower_triangular_matrix(matrix):
    lower_triangular_matrix = np.zeros((len(matrix), len(matrix)))
    for i in range(1, len(matrix)):
        for j in range(0, i):
            lower_triangular_matrix[i][j] = matrix[i][j]

    return lower_triangular_matrix


def get_upper_triangular_matrix(matrix):
    upper_triangular_matrix = np.zeros((len(matrix), len(matrix)))
    for i in range(len(matrix) - 1):
        for j in range(1 + i, len(matrix)):
            upper_triangular_matrix[i][j] = matrix[i][j]

    return upper_triangular_matrix


def get_t_matrix(matrix):
    inverse_diagonal_matrix = get_inverse_matrix(get_diagonal_matrix(matrix))
    for i in range(len(inverse_diagonal_matrix)):
        for j in range(len(inverse_diagonal_matrix)):
            inverse_diagonal_matrix[i][j] *= -1
    lower_triangular_matrix = get_lower_triangular_matrix(matrix)
    upper_triangular_matrix = get_upper_triangular_matrix(matrix)
    lower_triangular_matrix_plus_upper_triangular_matrix = np.zeros((len(matrix), len(matrix)))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            lower_triangular_matrix_plus_upper_triangular_matrix[i][j] = (
                    lower_triangular_matrix[i][j] + upper_triangular_matrix[i][j]
            )
    t_matrix = np.matmul(inverse_diagonal_matrix, lower_triangular_matrix_plus_upper_triangular_matrix)
    return t_matrix


def get_c_matrix(matrix, b):
    inverse_diagonal_matrix = get_inverse_matrix(get_diagonal_matrix(matrix))
    c_matrix = np.matmul(inverse_diagonal_matrix, b)
    return c_matrix


def get_augmented_matrix(matrix, b):
    augmented_matrix = np.zeros((len(matrix), len(matrix) + 1))
    for i in range(len(augmented_matrix)):
        for j in range(augmented_matrix.shape[1]):
            if j == len(augmented_matrix):
                augmented_matrix[i][j] = b[i]
            else:
                augmented_matrix[i][j] = matrix[i][j]

    return augmented_matrix


def check_solutions_number(matrix, b):
    augmented_matrix = get_augmented_matrix(matrix, b)
    matrix_rank = np.linalg.matrix_rank(matrix)
    augmented_matrix_rank = np.linalg.matrix_rank(augmented_matrix)
    unknowns_number = len(matrix)
    if matrix_rank == augmented_matrix_rank and matrix_rank == unknowns_number:
        return 1
    elif matrix_rank == augmented_matrix_rank and matrix_rank < unknowns_number:
        return float('inf')
    else:
        return 0
