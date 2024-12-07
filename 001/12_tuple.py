from loguru import logger

test_tple = (1,50,1,1,1,True,10.5,"vinay")
print(test_tple)
print(type(test_tple))

if 1 in test_tple:
    logger.info(f"1 vlaue is persent in tuple {test_tple}")

print(test_tple.count(1))
print(test_tple.index(50))
print(len(test_tple))

#
test_tuple=([5, 6], [6, 7, 8, 9],[3])
print(test_tuple)

result=()
for n in test_tuple:
    break_tuble = tuple(n)
    result=result+break_tuble
    print(break_tuble)
    print(result)
print(result)

result1=[]
for n1 in test_tuple:
    break_tuble1=n1
    result1=result1+break_tuble1
    print(break_tuble1)
    print(result1)
print(result1)


#2. Write a program to return a tuple which is
#exponential of given two tuples as an input

#Example: -
#Input: - tuple1 = (10, 12, 3, 5,6)
#tuple2 = (3, 6, 4, 3)
#Output: - (1000, 64, 81, 125)

tuple1 = (10, 2, 3, 5)
tuple2 = (3, 6, 4, 3)

final=()
for i in range(len(tuple1)):
    rslt=tuple1[i] ** tuple2[i]
    print(type(rslt))
    rslt1=(rslt,)
    print(type(rslt1))
    final=final+rslt1

print(final)