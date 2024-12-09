class mycar:
    def __init__(self,speed,color):
        self.speed = speed
        self.color = color
        print("End of __init__")

mycar(100,'red')

ford = mycar(500,'Yellow')
print("Ford Car Speed is: ",ford.speed)
print("Ford Car Color is: ",ford.color)

ford.speed = 1000

print("Ford Car Speed is: ",ford.speed)
print("Ford Car Color is: ",ford.color)

# ============================================================

class mycar_new:
    def __init__(self,speed,color):
        self.__speed = speed
        self.__color = color
        print("End of __init__")

    def set_speed(self,speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

tata = mycar_new(10,'orange')
tata.set_speed(500)
tata.speed =20
print(tata.get_speed())



