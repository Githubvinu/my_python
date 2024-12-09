from polygon import Ploygon
from shapes import Shape

class Tringale(Ploygon, Shape):# Sub Class
    def area(self):
        return self.get_weidth() * self.get_height() /2