class User:
    # Class atribute
    specie = "Human"
    
    def __init__(self, name, age):
        # Instance atributes
        self.name = name
        self.age = age
    
    def Hello(self):
        return f"My name is {self.name} and I'm {self.age} years old"


user = User("Andrew", 25)

print(user.Hello())

class Math:
    a = 6
    b = 2
    
    def __init__(self, c):
        self.c = c
        
    # Cant access any of the attributes, since its static
    @staticmethod
    def sum(a, b):
        return a + b
    
    @classmethod
    # Is changing the values of the original class
    def changeValues(cls):
        cls.a = 10
        cls.b = 10
    
    def divide(self):
        return (self.a / self.b) + self.c

print(Math.sum(4, 4))

calc = Math(3)
print(calc.divide())

Math.changeValues()

print(calc.divide())