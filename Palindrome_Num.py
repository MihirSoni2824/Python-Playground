# Function to check if a number is a palindrome
def is_palindrome(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")