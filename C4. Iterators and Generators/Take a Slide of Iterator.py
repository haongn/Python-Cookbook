# use itertools.islice() function: 

def count(n): 
    """This function increases its value non-stop."""
    while True: 
        yield n 
        n += 1 

c = count(0)

import itertools
for x in itertools.islice(c, 10, 20): 
    print(x)
    

