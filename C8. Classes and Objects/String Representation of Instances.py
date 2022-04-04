class Pair: 
    def __init__(self, x, y): 
        self.x = x
        self.y = y 

    def __repr__(self) -> str:      # developer-friendly string representation
        return 'Pair({0.x!r}, {0.y!r})'.format(self)   # x and y attributes of argument 0 (self)

    def __str__(self) -> str:       # user-friendly string representation
        return '({0.x!s}, {0.y!s})'.format(self)       # x and y attributes of argument 0 (self)


if __name__ == '__main__':
    p = Pair(3, 4)
    print(repr(p))                # __repr__() output
    print(p)                      # __str__() output

    






