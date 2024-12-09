class hello:
    def __init__(self,name):
        self.a = 10
        self._b =20
        self.__c = 30
        self.namval = name
    def public_method(self):
        print(self.a)
        print(self._b)
        print(self.__c)
        print("Pulblc")
        self.__private_method()


    def __private_method(self):
        print("private")


myhello = hello("Welcome")
print(myhello.a)
print(myhello._b)
print(myhello.namval)
#print(myhello.__c)
print(myhello.public_method())
#print(myhello.__private_method())
