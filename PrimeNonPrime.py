# Function to check if a number is prime
def is_prime(num):
    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")