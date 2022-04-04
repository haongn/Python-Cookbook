# A simple way to customize access to an attribute is to define it as a “property.”. 
# This code defines a property that adds simple type checking to an attribute. 

class Person: 
    def __init__(self, first_name): 
        self.first_name = first_name

    # Getter function (access attribute)
    @property
    def first_name(self): 
        return self._first_name 

    # Setter function (change attribute)
    @first_name.setter
    def first_name(self, value): 
        if not isinstance(value, str): 
            raise TypeError('Expected a string.')
        
        self._first_name = value

    # Deleter function (optional) (delete attribute)
    @first_name.deleter
    def first_name(self): 
        raise AttributeError("Can't delete a attribute.")


if __name__=='__main__': 
    a = Person('Guido')       # Call the getter
    print(a.first_name)
    # a.first_name = 42         # Call the setter 
    del a.first_name

