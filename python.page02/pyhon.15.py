def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
num1 = 56
num2 = 98
gcd = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd}")
