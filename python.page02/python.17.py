# Start the loop
while True:
    number = int(input("Enter a number: "))

    # Multiply the number by 2
    while number <= 50:
        number *= 2
        print(f"Current number: {number}")

    # Check if the number is greater than 50
    if number > 50:
        break

print("The number is now greater than 50.")
