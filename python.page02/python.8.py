# Define the nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Use a for loop to iterate through each sublist and then through each element
for sublist in nested_list:
    for element in sublist:
        print(element)
