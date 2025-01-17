# Function to find a specific word in a string
def find_word(input_string, word):
    # Split the string into words
    words = input_string.split()
    # Check if the word exists in the list of words
    if word in words:
        return f"The word '{word}' was found in the string."
    else:
        return f"The word '{word}' was NOT found in the string."

# Input from the user
input_string = input("Enter a string: ")
word_to_find = input("Enter the word to find: ")

# Find the word
result = find_word(input_string, word_to_find)

# Output the result
print(result)