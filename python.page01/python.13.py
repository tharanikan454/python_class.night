def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

# Example usage
test_numbers = [3, 5, 15, 22, 30]
results = [fizz_buzz(num) for num in test_numbers]
print(results)
