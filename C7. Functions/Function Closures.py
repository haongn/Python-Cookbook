# Nested function can be easily accessed inside the outer function, but not outside of its body.
# Nested function are able to access variables of the outer function. This is called non-local 
# variables. 

def outerFunction(text): 
    text = text      # non-local variable 

    def innerFunction(): 
        print(text)

    innerFunction()  # call nested function inside the outer function's body

if __name__ == '__main__':
    outerFunction('Hey!')





