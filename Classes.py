class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Rex")
print(my_dog.bark())  
