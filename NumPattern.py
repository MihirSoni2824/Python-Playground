# Function to print the pattern
def print_pattern(n):
    for i in range(n, 0, -1):  # Loop for rows in reverse order
        # Print numbers from 1 to i
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # Move to the next line after each row

# Input number of rows
rows = int(input("Enter the number of rows: "))

# Print the pattern
print_pattern(rows)