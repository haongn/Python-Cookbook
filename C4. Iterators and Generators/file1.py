filename = ''

with open(filename) as f: 
    try: 
        while True: 
            line = next(f)       # move to the next line 
            print(line, end = '')
    except StopIteration:        # signal the end of iteration
        pass  


# instruct the program to return a terminating value instead (ie. None): 
with open(filename) as f: 
    while True:
        line = next(f, None)     # return None if there is no new line in f
        if line is None: 
            break 
        print(line, end = '')

    








