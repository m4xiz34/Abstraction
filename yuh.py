from abc import ABC, abstractmethod

class absclass(ABC):
    
    def print(self,x):
        print("Passed value:", x)
        
    @abstractmethod
    def task(self):
        print("Yoo we are inside Absclass")
        
class testclass(absclass):
    def task(self):
        print("Now we are inside test_class task")
        

test_obj = testclass()
test_obj.task()
test_obj.print(100)
