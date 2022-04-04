# Context managers: facilitate the proper handling of resources.
# This is a mechanism for the automatic setup and teardown of resources (file operations, 
# database connection). 

# Main Problem: make sure to release these resources after usage. 
# If they are not released then it will lead to resource leakage and may cause the system 
# to either slow down or crash.

# Context managers can be written using classes or functions(with decorators).


# file management
# filename = ''
# with open(filename) as f: 
#     data = f.read()

# Creating a Context Manager :

# When creating context managers using classes, user need to ensure that the class has the methods:
# __enter__() and __exit__(). 

# The __enter__() returns the resource that needs to be managed. 

# the __exit__() does not return anything but performs the cleanup operations.

class ContextManager(): 
    def __init__(self): 
        print('Init method called.')

    def __enter__(self): 
        print('Enter method called.')
        return self     
    
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        print('Exit method called.')


with ContextManager() as manager: 
    print('with statement block.')


# In this case a ContextManager object is created. This is assigned to the variable after the 
# as keyword i.e manager. On running the above program, the following get executed in sequence:

# __init__()
# __enter__()
# statement body (code inside the with block)
# __exit__()[the parameters in this method are used to manage exceptions]

