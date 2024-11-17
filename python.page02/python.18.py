# Predefined number to guess
correct_number = 452004

while True:
    # Prompt the user for a guess
    user_guess = int(input("Guess the number: "))

    # Check if the guess is correct
    if user_guess == correct_number:
        print("hii tharanikan how are you !")
        break
    else:
        print("Incorrect guess, please try again.")
