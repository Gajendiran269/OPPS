from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    def describe(self):
        print(f"This is a {self.__class__.__name__}")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"
    
    def move(self):
        return "Running on four legs"

class Bird(Animal):
    def make_sound(self):
        return "Chirp!"
    
    def move(self):
        return "Flying with wings"

# Usage
dog = Dog()
print(dog.make_sound())
dog.describe()

bird = Bird()
print(bird.make_sound())
bird.describe()