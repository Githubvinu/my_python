from rectangle import Rectangle
from triangle import Tringale

rect = Rectangle()
tri = Tringale()

rect.set_values(10,20)
tri.set_values(30,20)

rect.set_color('red')
tri.set_color('Blue')

print(rect.area())
print(tri.area())

print(rect.get_color())
print(tri.get_color())