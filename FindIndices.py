# Function to find indices of two numbers that add up to the target sum
def find_indices(nums, target):
    # Create a dictionary to store the difference and its index
    num_to_index = {}
    for index, num in enumerate(nums):
        # Calculate the difference needed to reach the target
        difference = target - num
        # Check if the difference is already in the dictionary
        if difference in num_to_index:
            return [num_to_index[difference], index]
        # Store the current number and its index in the dictionary
        num_to_index[num] = index
    return None  # Return None if no such pair is found

# Input array and target sum
nums = [2, 2, 3]
target = 5

# Find the indices
result = find_indices(nums, target)

# Output the result
if result:
    print(f"Indices of elements that sum to {target}: {result}")
else:
    print("No such pair found.")