# Function to replace a character at a specific index
def replace_char(input_string, index, new_char):
    # Check if the index is valid
    if index < 0 or index >= len(input_string):
        return "Invalid index"
    
    # Convert the string to a list (strings are immutable in Python)
    string_list = list(input_string)
    # Replace the character at the specified index
    string_list[index] = new_char
    # Convert the list back to a string
    return "".join(string_list)

# Input from the user
input_string = input("Enter a string: ")
index = int(input("Enter the index to replace: "))
new_char = input("Enter the new character: ")

# Replace the character
result = replace_char(input_string, index, new_char)

# Output the result
print("Modified string:", result)