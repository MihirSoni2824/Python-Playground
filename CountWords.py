# Function to count the number of words in a string
def count_words(input_string):
    # Split the string into words using spaces as the delimiter
    words = input_string.split()
    # Return the number of words
    return len(words)

# Input from the user
input_string = input("Enter a string: ")

# Count the number of words
word_count = count_words(input_string)

# Output the result
print("Number of words in the string:", word_count)