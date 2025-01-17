# Function to rotate a 3x3 matrix (transpose)
def rotate_matrix(matrix):
    # Use list comprehension to transpose the matrix
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Input 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Rotate the matrix
rotated_matrix = rotate_matrix(matrix)

# Output the original and rotated matrix
print("Original Matrix:")
for row in matrix:
    print(row)

print("\nRotated Matrix (Row to Column):")
for row in rotated_matrix:
    print(row)