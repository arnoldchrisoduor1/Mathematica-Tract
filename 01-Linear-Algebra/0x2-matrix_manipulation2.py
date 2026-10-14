import numpy as np

def multiply_matrices(matrix_left, matrix_right):
    matrix_left = np.asarray(matrix_left)
    matrix_right = np.asarray(matrix_right)
    
    if matrix_left.ndim !=2 or matrix_right.ndim != 2:
        raise ValueError("Both matrices must be 2-dimensional.")
    
    if matrix_left.shape[1] != matrix_right.shape[0]:
        raise ValueError(
            "The left matrix's column count must match"
            "the right matrix's row count"
            )
    return matrix_left @ matrix_right

matrix_left = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_right = [
    [7, 8],
    [9, 10],
    [11, 12]
]

product = multiply_matrices(matrix_left, matrix_right)
print(product)