from polygon import Ploygon
from shapes import Shape

class Rectangle(Ploygon, Shape):#sub class
    def area(self):
        return  self.get_weidth() * self.get_height()