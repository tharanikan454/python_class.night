def are_all_positive(numbers):
    for number in numbers:
        if number <= 0:
            return False
    return True

# Example usage
test_list = [1, 2, 3, 4, 5]
result = are_all_positive(test_list)
print(f"Are all numbers positive? {result}")
