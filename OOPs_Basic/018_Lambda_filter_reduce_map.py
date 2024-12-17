def double(x):
    return x * 2
def add(x,y):
    return x + y
def product(x,y,z):
    return x * y * z

a = double(10)
print("double(10): ",a)

b = add(50,20)
print("add(50,20): ",b)

c = product(2,3,4)
print("product(2,3,4): ",c)

print("========================LAMBDA========================")

doublel = lambda x : x *2
addl = lambda x, y : x + y
productl = lambda x,y,z : x * y * z

print(doublel(100))
print(addl(100,5))
print(productl(10,2,20))

my_list = [2,3,4,5,6]
add_list = map(lambda x:x*2,my_list)
print(list(add_list))

my_list_1 = (10,20,30,40,50)
my_list_2 = (1,2,3,4,5)
add_two_list = map(lambda x,y:x+y,my_list_1,my_list_2)
print(list(add_two_list))

my_list3 = [1,2,3,4,5,6,7,8,9,10,11]
evennum = filter(lambda x:x%2==0,my_list3)
print(list(evennum))

graterfive = filter(lambda x : True if x > 5 else False,my_list3)
print(list(graterfive))

print("==================Reduce===============")
from functools import reduce
my_list4 = (10,20,30,40,50)
listtotal = reduce(lambda x,y : x + y,my_list4)
print(listtotal)
