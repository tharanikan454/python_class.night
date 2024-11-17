def square_numbers(numbers):
    return [number ** 2 for number in numbers]

# Example usage
numbers_list = [1, 2, 3, 4, 5]
squared_list = square_numbers(numbers_list)
print("Original list:", numbers_list)
print("List of squares:", squared_list)
