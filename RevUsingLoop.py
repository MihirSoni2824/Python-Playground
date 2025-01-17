# Function to reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        # Extract the last digit
        digit = num % 10
        # Append the digit to the reversed number
        reversed_num = reversed_num * 10 + digit
        # Remove the last digit from the original number
        num = num // 10
    return reversed_num

# Input from the user
number = int(input("Enter a number: "))

# Reverse the number
reversed_number = reverse_number(number)

# Output the result
print(f"The reversed number is: {reversed_number}")