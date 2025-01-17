# Function to convert Roman numeral to integer
def roman_to_int(roman):
    # Dictionary to map Roman numerals to their integer values
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Iterate through the Roman numeral string from right to left
    for char in reversed(roman):
        current_value = roman_to_int_map[char]
        # If the current value is less than the previous value, subtract it
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    
    return total

# Input from the user
roman_numeral = input("Enter a Roman numeral: ").upper()

# Convert Roman numeral to integer
integer_value = roman_to_int(roman_numeral)

# Output the result
print(f"The integer value of {roman_numeral} is: {integer_value}")