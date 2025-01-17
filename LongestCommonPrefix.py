# Function to find the longest common prefix
def longest_common_prefix(strs):
    if not strs:  # Check if the input list is empty
        return ""
    
    # Find the shortest string in the list
    shortest_str = min(strs, key=len)
    
    # Iterate through the characters of the shortest string
    for i, char in enumerate(shortest_str):
        # Compare the character with the corresponding character in other strings
        for other_str in strs:
            if other_str[i] != char:
                return shortest_str[:i]  # Return the prefix up to the mismatch
    
    return shortest_str  # If no mismatch, return the entire shortest string

# Input list of strings
input_strings = ["Flower", "Flow", "Flight"]

# Find the longest common prefix
result = longest_common_prefix(input_strings)

# Output the result
print(f"The longest common prefix is: '{result}'")