# Function to check if a number is an Armstrong number
def is_armstrong(num):
    # Convert the number to a string to find the number of digits
    num_str = str(num)
    length = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_digits = sum(int(digit) ** length for digit in num_str)
    
    # Check if the sum is equal to the original number
    return sum_of_digits == num

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")