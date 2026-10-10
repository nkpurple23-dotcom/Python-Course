from abc import ABC,abstractmethod
class Animal(ABC):
    def move (self):
        pass
class Human(Animal):
    def move (self):
        print("I can run and walk.")
class Snake(Animal):
    def move (self):
        print("I can crawl.")
class Dog(Animal):
    def move (self):
        print("I can bark.")
class Lion(Animal):
    def move (self):
        print("I can roar.")
human=Human()
snake=Snake()
dog=Dog()
lion=Lion()
human.move()
snake.move()
dog.move()
lion.move()