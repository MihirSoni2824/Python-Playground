# Function to perform the "Count and Say" operation
def count_and_say(number):
    # Convert the number to a string for easy iteration
    number_str = str(number)
    result = ""
    i = 0
    n = len(number_str)
    
    while i < n:
        # Get the current digit
        current_digit = number_str[i]
        count = 1
        
        # Count the number of times the current digit repeats
        while i + 1 < n and number_str[i + 1] == current_digit:
            count += 1
            i += 1
        
        # Append the count and the digit to the result
        result += f"{count} {current_digit}{'s' if count > 1 else ''}, "
        i += 1
    
    # Remove the trailing comma and space
    return result.rstrip(", ")

# Input number
input_number = 332251

# Perform the "Count and Say" operation
output = count_and_say(input_number)

# Output the result
print(output)