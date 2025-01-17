# Function to remove vowels from a string
def remove_vowels(input_string):
    # Define vowels
    vowels = "aeiouAEIOU"
    # Use list comprehension to filter out vowels
    result_string = ''.join([char for char in input_string if char not in vowels])
    return result_string

# Input from the user
input_string = input("Enter a string: ")

# Remove vowels
result = remove_vowels(input_string)

# Output the result
print("String after removing vowels:", result)