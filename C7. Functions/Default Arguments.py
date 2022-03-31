# Simply assign values in the definition and make sure that default arguments appear last.

def spam(a, b = 42):     # default argument appears last
    print(a, b)

spam(1)        # a = 1, b = 42
spam(1, 2)     # a = 1, b = 2 

# If the default value is supposed to be a mutable container, such as a list, set, or dictionary,
# use None as the default and write code like this:

def spam(a, b = None): 
    # Using a list as a default value: 
    if b is None: 
        b = []
    pass 

# If, instead of providing a default value, you want to write code that merely tests whether
# an optional argument was given an interesting value or not, use this idiom: 
_no_value = object()

def spam(a, b = _no_value): 
    if b is _no_value:
        print('No b value supplied')
    pass     
    
spam(1)
spam(1, 2)        # b = 2
spam(1, None)     # b = None 





