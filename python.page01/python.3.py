def is_palindrome(string):
    # Remove any non-alphanumeric characters and convert to lowercase
    clean_string = ''.join(char.lower() for char in string if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return clean_string == clean_string[::-1]


# Example usage
test_string = "A man, a plan, a canal, Panama"
result = is_palindrome(test_string)
print(f'Is "{test_string}" a palindrome?', result)
