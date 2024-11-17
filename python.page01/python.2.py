def find_largest_number(numbers):
    if not numbers:  # Check if the list is empty
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Example usage
numbers_list = [3, 1, 56, 32, 78, 12]
result = find_largest_number(numbers_list)
print("The largest number is:", result)
