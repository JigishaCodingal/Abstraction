# Import necessary Modules
from abc import ABC, abstractmethod
# Create base class
class A(ABC):
	# Function to print a value
    def print(self,x):
        print("Passed value: ", x)
	# Abstract Method
    @abstractmethod
    def task(self):
        pass        
# Create sub class
class B(A):
    def task(self):
        print("We are inside test_class task")
#object of test_class created
obj = B()
obj.task()
obj.print(100)