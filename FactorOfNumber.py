# Function to find factors of a number
def find_factors(num):
    factors = []
    # Iterate from 1 to the number itself
    for i in range(1, num + 1):
        if num % i == 0:  # Check if 'i' is a factor
            factors.append(i)
    return factors

# Input from the user
number = int(input("Enter a number: "))

# Find and print the factors
factors = find_factors(number)
print(f"The factors of {number} are: {factors}")