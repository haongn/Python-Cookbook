# reversed iteration can be customized on user-defined classes if they implement the 
# __reverse__() method.

class Countdown:
    def __init__(self, start): 
        self._start = start

    # Forward iterator: 
    def __iter__(self): 
        n = self._start
        while n > 0: 
            yield n 
            n -= 1 

    # Reverse iterator: 
    def __reverse__(self): 
        n = 1 
        while n <= self._start:
            yield n 
            n += 1 


if __name__ == '__main__':
    c = Countdown(5)
    for n in c:        # implement __iter__() method 
        print(n)       # forward iteration (no StopIteration raise automatically)
    
    for n in c.__reverse__():    
        print(n)








