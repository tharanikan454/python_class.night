# Initialize the first two numbers of the Fibonacci sequence
a, b = 0, 1

# Use a for loop to print the first 10 numbers in the Fibonacci sequence
for _ in range(10):
    print(a)
    a, b = b, a + b
