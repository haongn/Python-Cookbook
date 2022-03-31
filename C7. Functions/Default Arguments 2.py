# 1. The default value was fixed at function definition time, i.e, it cannot be change afterwards.

x = 42 
def spam(a, b = x):    # the default value is fixed at the time of function definition 
    print(a, b)

spam(1)

x = 23            # has no effect on the default value, i.e, the default value's not changed
spam(1)

# 2. The values assigned as defaults should always be immutable objects 
#    (None, True, False, numbers, strings)

# Never write code like this: 
def spam(a, b = []):      # NO!
    pass 

