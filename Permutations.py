# Function to find all permutations recursively
def find_permutations(input_list):
    if len(input_list) == 0:
        return []
    if len(input_list) == 1:
        return [input_list]
    
    # List to store all permutations
    result = []
    
    for i in range(len(input_list)):
        # Extract the current element
        current_element = input_list[i]
        # Remaining list after removing the current element
        remaining_list = input_list[:i] + input_list[i+1:]
        # Generate all permutations of the remaining list
        for perm in find_permutations(remaining_list):
            result.append([current_element] + perm)
    
    return result

# Input list
input_list = [1, 2, 3]

# Find all permutations
permutation_list = find_permutations(input_list)

# Output the result
print("All permutations of", input_list, "are:")
for perm in permutation_list:
    print(perm)