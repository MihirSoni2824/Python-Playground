# Input two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Swap the strings without using a third variable
string1, string2 = string2, string1

# Output the swapped strings
print("After swapping:")
print("First string:", string1)
print("Second string:", string2)