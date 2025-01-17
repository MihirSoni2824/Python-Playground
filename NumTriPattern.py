# Function to print the pattern
def print_pattern(n):
    for i in range(1, n + 1):  # Loop for rows
        for j in range(1, i + 1):  # Loop for columns
            print(j, end=" ")  # Print numbers from 1 to i
        print()  # Move to the next line after each row

# Input number of rows
rows = int(input("Enter the number of rows: "))

# Print the pattern
print_pattern(rows)