class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Hello(self):
        return f"My name is {self.name} and I'm {self.age} years old"


user = User("Andrew", 25)

print(user.Hello())