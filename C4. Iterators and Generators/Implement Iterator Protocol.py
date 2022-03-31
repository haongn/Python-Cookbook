# Implement Depth-First Search (DFS) 


class Node: 
    """Implement an iterator that traverses nodes in a depth-first pattern."""
    def __init__(self, value): 
        self._value = value 
        self._children = []             # set list as underlying container 

    def __repr__(self):                 # object's representation of this class
        return 'Node({!r})'.format(self._value)

    def add_child(self, node): 
        self._children.append(node)     # append new node to the list 
        
    def __iter__(self): 
        return iter(self._children)     # invoke __iter__() method 

    def depth_first(self): 
        yield self  
        for c in self:          # implement __iter__() method => lap qua Node con cua self
            yield from c.depth_first()  # yield node theo thu tu thu tren xuong 


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root.depth_first():   # iterating over the generator
        print(ch)




            