# @property decorator: a pythonic way to use getter and setter in OOP. 
# @property decorator: makes use of getter and setters much easier in OOP. 

# Class without Getters and Setters: 
# Basic method of getting and setting attributes in Python: 
class Celcius: 
    def __init__(self, temperature = 0): 
        self.temperature = temperature

    def to_fahrenheit(self): 
        return (self.temperature * 1.8) + 32


# Create a new object: 
human = Celcius()

# Set the temperature: 
human.temperature = 37

# Get the temperature attribute: 
print(human.temperature)

# Get the to_fahrenheit method: 
print(human.to_fahrenheit())

# Whenever we assign or retrieve any object attribute like temperature as shown above, 
# Python searches it in the object's built-in __dict__ dictionary attribute.
print(human.__dict__)
# Therefore, man.temperature internally becomes man.__dict__['temperature'].






