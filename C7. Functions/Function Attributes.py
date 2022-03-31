def add(x: int, y: int) -> int:    # this is just hints, not type checks 
    return x + y 


if __name__ == '__main__':
    print(add.__class__)         # class function
    print(add.__closure__)       # bao đóng???
    print(add.__code__)
    print(add.__dict__)
    print(add.__defaults__)
    print(add.__doc__)
    print(add.__format__)
    print(add.__globals__)
    print(locals())
    print(globals())