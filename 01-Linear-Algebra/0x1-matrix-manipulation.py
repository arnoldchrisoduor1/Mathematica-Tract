def multiply_matrices(matrix_left, matrix_right):
    if not matrix_left or not matrix_right:
        raise ValueError("Matrices must not be empty.")
    
    left_columns = len(matrix_left[0])
    right_columns = len(matrix_right[0])
    
    if left_columns or right_columns == 0:
        raise ValueError("matrices must have atleast one column")
    
    if any(len(row) != left_columns for row in matrix_left):
        raise ValueError("The left matrix must be rectangular")
    
    if any(len(row) != right_columns for row in matrix_right):
        raise ValueError("The right matrix must be rectangular")