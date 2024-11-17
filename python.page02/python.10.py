# Start the loop
while True:
    user_input = input("Please enter something (type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("poyrru vangkoo!")
        break
    else:
        print(f"You entered: {user_input}")
