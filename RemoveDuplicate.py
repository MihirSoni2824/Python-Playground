def remove_duplicates(input_string):
    seen = set()
    result = []
    for char in input_string:
        if char.lower() not in seen:  # Convert to lowercase for case-insensitivity
            seen.add(char.lower())
            result.append(char)
    return ''.join(result)

input_string = input("Enter a string: ")
result = remove_duplicates(input_string)
print("String after removing duplicates:", result)