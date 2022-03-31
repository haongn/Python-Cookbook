# mình đang không hiểu extra state ở đây có nghĩa là gì???

# prob: You would like to define a generator function, but it involves extra state that you  
# would like to expose to the user somehow.

# sol: If you want a generator to expose extra state to the user, don’t forget that you can 
# easily implement it as a class, putting the generator function code in the __iter__() method.

from collections import deque   

class linehistory: 
    def __init__(self, lines, histlen = 3): 
        self.lines = lines
        self.history = deque(maxlen = histlen)

    def __iter__(self):      # put the generator function in the __iter__() method 
        for lineno, line in enumerate(self.lines, 1): 
            self.history.append((lineno, line))
            yield line 
        
    def clear(self): 
        self.history.clear()


if __name__ == '__main__':
    filename = ''
    with open(filename) as f:    
        lines = linehistory(f)    # create an instance
        for line in lines:        # iterate over each line of the file 
            if 'python' in line: 
                for lineno, hline in lines.history: 
                    print('{}{}'.format(lineno, hline), end = '')


                    
            