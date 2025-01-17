# Function to print the Right Pascal's Triangle
def print_right_pascal(n):
    # Upper part of the triangle
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()  # Move to the next line after each row

    # Lower part of the triangle
    for i in range(n - 1, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()  # Move to the next line after each row

# Input number of rows for the upper half
rows = int(input("Enter the number of rows for the upper half: "))

# Print the Right Pascal's Triangle
print_right_pascal(rows)