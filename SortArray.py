# Function to sort an array in place
def sort_array(arr):
    arr.sort()  # Sort the array in place

# Input array from the user
input_array = input("Enter elements of the array (comma-separated): ").split(",")
input_array = [int(item.strip()) for item in input_array]  # Convert to integers

# Sort the array in place
sort_array(input_array)

# Output the sorted array
print("Sorted array:", input_array)