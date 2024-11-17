# Initialize the sum
total_sum = 0

while True:
    # Prompt the user for input
    number = int(input("Enter a number: "))

    # Check if the number is greater than 100
    if number > 100:
        break

    # Add the number to the total sum
    total_sum += number

# Print the final sum
print(f"The sum of the numbers you entered is: {total_sum}")
