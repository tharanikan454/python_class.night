def count_vowels(input_string):
    # Convert the string to lowercase to make the function case-insensitive
    input_string = input_string.lower()
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    # Initialize a counter
    count = 0
    # Iterate through each character in the string
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# Example usage
test_string = "Hello World"
result = count_vowels(test_string)
print(f"The number of vowels in '{test_string}' is: {result}")
