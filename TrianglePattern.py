# Function to print the triangle pattern with spacing
def print_triangle_pattern(n):
    num = 1  # Initialize the starting number
    for i in range(1, n + 1):  # Loop for rows
        # Print spaces for alignment
        for j in range(n - i):
            print(" ", end="  ")
        # Print numbers with spacing
        for k in range(i):
            print(num, end="   ")  # Add extra spaces between numbers
            num += 1  # Increment the number
        print()  # Move to the next line after each row

# Input number of rows
rows = int(input("Enter the number of rows: "))

# Print the triangle pattern
print_triangle_pattern(rows)