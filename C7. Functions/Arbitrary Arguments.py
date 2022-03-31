# Writing a function that accept any number of (positional) arguments: 

# Sol: use a * argument. 

def avg(first, *rest):     #  rest is a tuple of all the extra positional arguments passed
    return (first + sum(rest)) / (1 + len(rest))


if __name__ == '__main__':
    result = avg(1, 2)
    print(result)
    result = avg(1, 2, 3, 4)
    print(result)

    