class Ploygon:#super calss
    __width = None
    __height = None

    def set_values(self,widht,height):
        self.__width = widht
        self.__height = height
    def get_weidth(self):
        return self.__width
    def get_height(self):
        return self.__height
    
class Rectangle(Ploygon):#sub class
    def area(self):
        return  self.get_weidth() * self.get_height()

    
class Tringale(Ploygon):# Sub Class
    def area(self):
        return self.get_weidth() * self.get_height() /2
    
rect = Rectangle()
tri = Tringale()
rect.set_values(10,10)
tri.set_values(20,20)

print(rect.area())
print(tri.area())