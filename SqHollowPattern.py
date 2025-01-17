# Function to draw a square hollow pattern
def draw_square_hollow(n):
    for i in range(n):  # Loop for rows
        for j in range(n):  # Loop for columns
            # Print '*' for the first and last row, or first and last column
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")  # Print space for the hollow part
        print()  # Move to the next line after each row

# Input size of the square
size = int(input("Enter the size of the square: "))

# Draw the square hollow pattern
draw_square_hollow(size)