# Function to find GCD using the Euclidean Algorithm
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Update a to b and b to the remainder of a divided by b
    return a

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the GCD
gcd = find_gcd(num1, num2)

# Output the result
print(f"The GCD of {num1} and {num2} is: {gcd}")