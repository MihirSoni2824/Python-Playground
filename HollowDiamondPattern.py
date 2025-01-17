# Function to print the hollow diamond pattern
def print_hollow_diamond(n):
    # Upper part of the diamond
    for i in range(1, n + 1):
        # Print spaces for alignment
        for j in range(n - i):
            print(" ", end="")
        # Print asterisks and spaces
        for k in range(2 * i - 1):
            if k == 0 or k == 2 * i - 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line after each row

    # Lower part of the diamond
    for i in range(n - 1, 0, -1):
        # Print spaces for alignment
        for j in range(n - i):
            print(" ", end="")
        # Print asterisks and spaces
        for k in range(2 * i - 1):
            if k == 0 or k == 2 * i - 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line after each row

# Input number of rows (for the upper half)
rows = int(input("Enter the number of rows for the upper half: "))

# Print the hollow diamond pattern
print_hollow_diamond(rows)