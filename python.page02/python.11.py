# Prompt the user for input
user_number = int(input("Enter a number: "))

# Initialize variables
total_sum = 0
current_number = 1

# Use a while loop to calculate the sum
while current_number <= user_number:
    total_sum += current_number
    current_number += 1

# Print the result
print(f"The sum of all numbers from 1 to {user_number} is: {total_sum}")
