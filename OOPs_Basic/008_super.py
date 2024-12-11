class parent:
    def __init__(self):
        print("Parent __init__")
    def test(self,name):
        print("test ,",name)

class parent_2:
    def __init__(self):
        print("Parent2 __init__")

class child(parent,parent_2):
    def __init__(self):
        print("Child __init__")
        super().__init__()
        super().test('vinay')
        parent_2.__init__(self)
        parent.test(self,'sharma')

childobj = child()
print(child.__mro__)