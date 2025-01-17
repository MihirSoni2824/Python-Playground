# Function to check if a string is in Camel Case
def is_camel_case(input_string):
    if not input_string:  # Check if the string is empty
        return False
    # Check if the first character is lowercase and there are no spaces or underscores
    if input_string[0].isupper() or ' ' in input_string or '_' in input_string:
        return False
    # Check if there is at least one uppercase letter (Camel Case requirement)
    return any(char.isupper() for char in input_string)

# Input from the user
input_string = input("Enter a string: ")

# Check if the string is in Camel Case
if is_camel_case(input_string):
    print(f"'{input_string}' is in Camel Case.")
else:
    print(f"'{input_string}' is NOT in Camel Case.")