#Default Argument Values in Functions
def my_function(optional_param=None):
    if optional_param is None:
        optional_param = []
    optional_param.append(1)
    return optional_param

print(my_function())
print(my_function([2, 3]))



#Indicating Missing or Not Applicable Values




user_profile = {
    'name': 'tharanikan',
    'age': 20,
    'nickname': None
}

if user_profile['nickname'] is None:
    print("Nickname is not set.")


#Resetting Variables
my_var = 42
my_var = None






#Function Return Values When No Result is Needed

def find_element(element, collection):
    for item in collection:
        if item == element:
            return item
    return None

result = find_element(3, [1, 2, 4, 5])
if result is None:
    print("not found.")
