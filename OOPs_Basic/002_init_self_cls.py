class Car:
    def __init__(self, speed , color):
        print(speed)
        print(color)

class Carnew:
    def __init__(self, speed , color):
        print(speed)
        print(color)
        self.speed = speed
        self.color = color

ford = Car(200,'red')
tata = Car(300,'orange')

ford1 = Carnew(200,'black')
honda1 = Carnew(300,'white')

print("======")
print(ford1.speed)
print(honda1.color)


print("========Rectangle Class============")
class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width

ract1 = Rectangle(10,20)
ract2 = Rectangle(2,8)

print("ract1 value is :",ract1.height * ract1.width)
print("ract2 value is :",ract2.height * ract2.width)