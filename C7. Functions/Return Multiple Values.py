def myfun(): return 1, 2, 3        # return a tuple 


if __name__ == '__main__':
    a, b, c = myfun()              # tuple unpacking 
    x = myfun()                    # return a tuple 

    print(a)
    print(b)
    print(c)
    print(x)

