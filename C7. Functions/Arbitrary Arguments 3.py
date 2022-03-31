# If you want a function that can accept both any number of positional and keyword-only
# arguments, use * and ** together.

def anyargs(*args, **kwargs): 
    print(args)      # a tuple 
    print(kwargs)    # a dict 


if __name__ == '__main__':
    anyargs(10, 20, 'hello', name = 'Hao', age = 22, status = 'single')
    