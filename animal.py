from abc import ABC, abstractmethod

class Animal(ABC):
    
    def move(self):
        print("Blocktales")
        
class Human(Animal):
        
        def move(self):
            print("I can walk and run :D")
            
class Snake(Animal):
        
        def move(self):
            print("I can survive 5 minute after my head has been detached from my body.")

class Dog(Animal):
   def move(self):
           print("I can't eat chocolate :(")
           
class Lion(Animal):
   def move(self):
           print("No I am not from the Lion King.")

H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

L = Lion()
L.move()
