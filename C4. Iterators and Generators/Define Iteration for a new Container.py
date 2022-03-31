# Problem: You have built a custom container object that internally holds a list, tuple, or 
# some other iterable. You would like to make iteration work with your new container. You

# Solution: Typically, all you need to do is define an __iter__() method that delegates iteration 
# to the internally held container.

class Node: 
    def __init__(self, value): 
        self._value = value 
        self._children = []          # set list as underlying container 

    def __repr__(self):              # object's representation of this class
        return 'Node({!r})'.format(self._value)

    def add_child(self, node): 
        self._children.append(node)  # append new node to the list 
        
    def __iter__(self): 
        return iter(self._children)   # invoke __iter__() method 


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    
    root.add_child(child1)
    root.add_child(child2)

    for ch in root:           # vi da dinh nghia __iter__ o tren nen co the dung vong lap for
        print(ch)                     # invoke __repr__() method 

    # output Node(1), Node(2)





    


