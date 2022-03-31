# If you want to implement a new kind of iteration pattern, define it using a generator function. 

def frange(start, stop, increment): 
    """A generator that produces a range of floating-point numbers."""
    x = start 
    while x < stop: 
        yield x 
        x += increment   


# To use generator function, you iterate over it using a for loop or use it with some other
# function that consumes an iterable (e.g., sum(), list(), etc.)

if __name__ == '__main__':
    for n in frange(0, 4, 0.5):      # iterate over a generator function using a for loop
        print(n)                   

    result = list(frange(0, 1, 0.125))    # use a function that consume an iterable 
    print(result)


