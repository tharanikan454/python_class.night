def check_vowel_or_consonant(char):
    vowels = 'aeiouAEIOU'
    if len(char) != 1:
        return "Please provide a single character."
    if char.isalpha():
        if char in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Not an alphabetic character"

# Example usage
char = 'A'
result = check_vowel_or_consonant(char)
print(f"The character '{char}' is a {result}.")
