def my_func():
    yield 'a'
    yield 'b'
    yield 'c'

def my_func1():
    n = 1
    print("==================",n)
    yield n
    n +=1
    print("==================",n)
    yield n
    n +=1
    print("==================",n)
    yield n
    
def my_func2():
   for i in range(5):
       print('------------',i)
       yield i

    

x = my_func()
print(next(x))
print(next(x))
print(next(x))


x1 = my_func1()
print(next(x1))
print(next(x1))
print(next(x1))


x2 = my_func2()
print(next(x2))
print(next(x2))
print(next(x2))
print(next(x2))
print(next(x2))

print("=============SAME iterator coe in generator")
def list_iterator(list):
    for i in list:
        yield i

a = [1,2,3,6,4,7]
mylist =  list_iterator(a)
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))


for x in mylist:
    print(x)

