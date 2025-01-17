# Function to print the reverse pattern
def print_reverse_pattern(n):
    for i in range(1, n + 1):  # Loop for rows
        # Print spaces for alignment
        for j in range(n - i):
            print(" ", end=" ")
        # Print the numbers
        for k in range(i):
            print(i, end=" ")
        print()  # Move to the next line after each row

# Input number of rows
rows = int(input("Enter the number of rows: "))

# Print the reverse pattern
print_reverse_pattern(rows)