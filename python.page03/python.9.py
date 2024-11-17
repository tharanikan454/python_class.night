#Tuple Unpacking
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)


#List Unpacking
x, y, z = [4, 5, 6]
print(x)
print(y)
print(z)

#Using the Same Value
p = q = r = 7
print(p)
print(q)
print(r)

#Using a Function that Returns Multiple Values
def get_coordinates():
    return 10, 20

latitude, longitude = get_coordinates()
print(latitude)
print(longitude)

#Using a Function that Returns Multiple Values
def get_coordinates():
    return 10, 20

latitude, longitude = get_coordinates()
print(latitude)
print(longitude)

#Swapping Variables
a, b = 1, 2
a, b = b, a
print(a)  
print(b)



