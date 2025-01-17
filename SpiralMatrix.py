# Function to print a spiral matrix
def print_spiral_matrix(n):
    # Initialize a n x n matrix with zeros
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    # Define starting positions and boundaries
    left, right = 0, n - 1
    top, bottom = 0, n - 1
    num = 1  # Starting number

    while left <= right and top <= bottom:
        # Traverse from left to right (top row)
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Traverse from top to bottom (right column)
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Traverse from right to left (bottom row)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # Traverse from bottom to top (left column)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    # Print the spiral matrix
    for row in matrix:
        print(" ".join(map(str, row)))

# Input size of the matrix
size = int(input("Enter the size of the matrix: "))

# Print the spiral matrix
print_spiral_matrix(size)