# Using Getters and Setters

# Making Getters and Setters methods: 
# (Bản chất là dùng một hàm riêng biệt để lấy và đặt giá trị của nhiệt độ)
class Celsius: 
    def __init__(self, temperature = 0): 
        self.set_temperature(temperature)    # use the defined below function

    def to_fahrenheit(self): 
        return (self.get_temperature() * 1.8) + 32   # use the defined below function 

    # getter method 
    def get_temperature(self): 
        return self._temperature 

    # setter method 
    def set_temperature(self, value): 
        if value < -273.15: 
            raise ValueError('Temperature below -273.15 is not possible.')

        self._temperature = value 


# As we can see, the above method introduces two new get_temperature() and set_temperature() 
# methods.

# Furthermore, temperature was replaced with _temperature (private variable)

# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature())

# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())

# new constraint implementation
human.set_temperature(-300)

# Get the to_fahreheit method
print(human.to_fahrenheit())

# However, the bigger problem with the above update is that all the programs that implemented 
# our previous class have to modify their code from obj.temperature to obj.get_temperature() 
# and all expressions like obj.temperature = val to obj.set_temperature(val).

# This refactoring can cause problems while dealing with hundreds of thousands of lines of codes.

# All in all, our new update was not backwards compatible. This is where @property comes to rescue.





