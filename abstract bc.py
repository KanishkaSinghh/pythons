from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class rectangle(shape):
    type="rectangle"
    sides=4
    def __init__(self):
        self.length=8
        self.breadth=8
    def printarea(self):
        return self.length * self.breadth

rec1 = rectangle()
print(rec1.printarea())