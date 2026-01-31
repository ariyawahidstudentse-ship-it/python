from abc import ABC, abstractmethod

class Animal(ABC):

    def move(self):
        pass

class Human(Animal):

    def move(self):
        print("humans can walk and run")

class Snake(Animal):

    def move(self):
        print("snakes can crawl")

class Dog(Animal):

    def move(self):
        print("dogs can bark")

class lion(Animal):

    def move(self):
        print("lions can roar")

r = Human()
r.move()

k = Snake()
k.move()

r = Dog()
r.move()

k = lion()
k.move()
