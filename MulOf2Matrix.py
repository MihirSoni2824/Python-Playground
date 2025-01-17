# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        return "Matrices cannot be multiplied. Number of columns in the first matrix must equal the number of rows in the second matrix."
    
    # Initialize a result matrix with zeros
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    
    # Perform multiplication
    for i in range(len(matrix1)):  # Rows of matrix1
        for j in range(len(matrix2[0])):  # Columns of matrix2
            for k in range(len(matrix2)):  # Rows of matrix2
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

# Input matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Multiply the matrices
result = multiply_matrices(matrix1, matrix2)

# Output the result
if isinstance(result, str):
    print(result)
else:
    print("Product of the matrices:")
    for row in result:
        print(row)