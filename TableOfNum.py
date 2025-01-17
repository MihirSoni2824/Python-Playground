# Input from the user
number = int(input("Enter a number: "))
limit = int(input("Enter the limit for the table: "))

# Print the multiplication table
print(f"Multiplication table of {number}:")
for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")