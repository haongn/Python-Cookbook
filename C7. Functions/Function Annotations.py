# Although there are many potential uses of annotations, their primary utility is probably
# just documentation.
# Annotations can be used to implement multiple dispatch (i.e, overloaded function)

def add(x: int, y: int) -> int:    # this is just hints, not type checks 
    return x + y 


if __name__ == '__main__':
    print(add.__annotations__)


