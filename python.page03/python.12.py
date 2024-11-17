#Assigning values to multiple variables
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)


#Assigning the same value to multiple variables
x = y = z = 100
print(x)
print(y)
print(z)


#Swapping values between variables
m, n = 5, 10
m, n = n, m
print(m)
print(n)



#Using a function that returns multiple values
def get_coordinates():
    return 50, 75

latitude, longitude = get_coordinates()
print(latitude)
print(longitude)
