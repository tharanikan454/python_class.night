def has_pair_with_sum(numbers, target_sum):
    seen_numbers = set()
    for number in numbers:
        complement = target_sum - number
        if complement in seen_numbers:
            return True
        seen_numbers.add(number)
    return False

# Example usage
numbers_list = [2, 4, 3, 5, 7, 8, 9]
target = 10
result = has_pair_with_sum(numbers_list, target)
print(f"Does the list have a pair with sum {target}? {result}")
