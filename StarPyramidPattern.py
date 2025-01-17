# Function to print the pyramid pattern
def print_pyramid(n):
    for i in range(1, n + 1):  # Loop for rows
        # Print spaces for alignment
        for j in range(n - i):
            print(" ", end=" ")
        # Print asterisks
        for k in range(2 * i - 1):
            print("*", end=" ")
        print()  # Move to the next line after each row

# Input number of rows
rows = int(input("Enter the number of rows: "))

# Print the pyramid pattern
print_pyramid(rows)