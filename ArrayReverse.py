# Function to reverse an array in place
def reverse_array(arr):
    arr.reverse()  # Reverse the array in place

# Input array from the user
input_array = input("Enter elements of the array (comma-separated): ").split(",")
input_array = [item.strip() for item in input_array]  # Remove extra spaces

# Reverse the array in place
reverse_array(input_array)

# Output the reversed array
print("Reversed array:", input_array)