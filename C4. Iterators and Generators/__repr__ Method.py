# __repr__: used to represent a class's object as a string. 
# __repr__ is called by the repr() built-in function.
# You can define your own string representation of your class using the __repr__ method. 

# __repr__: (representation) represent object (of a class) as a string.
# __repr__: return a string as a representation of the object. 

# Ideally, the representation should be information-rich and could be used to recreate 
# an object with the same value.

class Person: 
    def __init__(self, name, age): 
        self._name = name 
        self._age = age
        
    def __repr__(self): 
        return 'Person(' + self._name + ', ' + str(self._age) + ')'
        

if __name__ == '__main__':
    person = Person('Hao', 22)
    print(repr(person))          # call the built-in function repr()
    print(person.__repr__())     # call the special method __repr__()
    print(person)

    

