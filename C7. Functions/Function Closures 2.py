# A Closure is a function object that remembers values in enclosing scopes 
# even if they are not present in memory. 

def outerFunction(text): 
    text = text 

    def innerFunction(): 
        print(text)

    # Note: We are returning function WITHOUT parenthesis 
    return innerFunction


if __name__=='__main__': 
    myFunction = outerFunction('Hey!')
    myFunction()