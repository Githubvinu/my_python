from loguru import logger
logger.info("********Lec-16_Tuple*******")

test_tuple = (1,2,3,4,5,'hello',True,'World',12.40,False)
print(test_tuple)
print(test_tuple[0])
print(test_tuple[:5])
print(test_tuple[3:7])
print(test_tuple[5:])
print(test_tuple[::-1])
print(test_tuple[::-3])

New_tuple = (1,2,3,4,5,'hello',True,'World',12.40,False,2,1,5,12.40,2)
print(New_tuple.count(2))
print(New_tuple.count(12.40))
print(len(New_tuple))
print(New_tuple.index('hello'))


#1. Write a program to return entire element as a tuple which
#can have a list in the tuple inputs.
#Example: -
#Input :- test_tuple = ([5, 6], [6, 7, 8, 9], [3])
#Output :- (5, 6, 6, 7, 8, 9, 3)
#Also talk about the time and space complexity


tuple01 = ([5, 6], [6, 7, 8, 9], [3],'hello')
print(tuple01)
print(type(tuple01[3]))
# way
Output=[]
for name in tuple01:
    if isinstance(name,list):
         Output.extend(name)
    else:
         Output.append(name)
         
print(Output)

new_output = tuple(Output)
print(new_output)


#2. Write a program to return a tuple which is
#exponential of given two tuples as an input
#Example: -
#Input: -
# tuple1 = (10, 2, 3, 5)
# tuple2 = (3, 6, 4, 3)
#Output: - (1000, 64, 81, 125)

tpl1 = (10, 2, 3, 5)
tpl2 = (3, 6, 4, 3)
rslt_tpl = ()
rslt_lst = []
for i in range(len(tpl1)):
    result = tpl1[i] ** tpl2[i]
    rslt_tpl = rslt_tpl + (result,)
    rslt_lst = rslt_lst + [result]
print(rslt_tpl)
print(rslt_lst)

