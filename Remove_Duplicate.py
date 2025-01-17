# Function to remove duplicate elements
def remove_duplicates(elements):
    # Use a set to store unique elements while preserving order
    unique_elements = []
    seen = set()
    for element in elements:
        if element not in seen:
            seen.add(element)
            unique_elements.append(element)
    return unique_elements

# Input list with duplicate elements
elements = input("Enter elements (comma-separated): ").split(",")
elements = [item.strip() for item in elements]  # Remove extra spaces

# Remove duplicates
result = remove_duplicates(elements)

# Output the result
print("Elements after removing duplicates:", result)