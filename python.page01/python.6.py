def remove_duplicates(input_list):
    # Using a set to store unique elements
    unique_elements = list(set(input_list))
    return unique_elements

# Example usage
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(original_list)
print("Original list:", original_list)
print("List with unique elements:", unique_list)
