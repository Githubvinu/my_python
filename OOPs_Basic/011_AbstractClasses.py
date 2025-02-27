from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimiter(self): pass

class Square(Shape):
    def __init__(self,side):
        self.__side = side
    def area(self):
        return self.__side * self.__side
    def perimiter(self):
        return 4 * self.__side


squire = Square(5)
print(squire.area())
print(squire.perimiter())