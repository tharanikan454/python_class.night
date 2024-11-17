#Local Variables
def my_function():
    local_var = 10
    print(local_var)

my_function()




#Global Variables
global_var = 20

def my_function():
    print(global_var)

my_function()
print(global_var)




#Modifying a Global Variable
global_var = 20

def modify_global():
    global global_var
    global_var = 30

modify_global()
print(global_var)
