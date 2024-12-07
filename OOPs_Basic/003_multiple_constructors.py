class Hello:
    def __init__(self,name='sonu'):
        print('__init Hello__')
        print(name)        


Hello('vinay')
Hello()

class Hellonew:
    def __init__(self, *args , **kwargs) :
        print('__init Hellonew__')       

Hellonew()
Hellonew('vinay')
Hellonew('vinay','sonu','a',myname='gannu')


class testhello:
    def __init__(self,name):
        self.name = name
        self.age = 25
        print(self.name,self.age)

testhello('sonu')