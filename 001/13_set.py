from loguru import logger

set_var={}
print(type(set_var))


set_variable ={1,2,7,8,4,12}
print(set_variable)

for i in set_variable:
    print(f"set vailable value is: {i}")

New_set_variable ={2,4,6,5,15}

print(set_variable)
print(New_set_variable)

print(f"union of two set is {set_variable.union(New_set_variable)}")
print(f"intersection of two set is {set_variable.intersection(New_set_variable)}")
print(f"difference of two set is {set_variable.difference(New_set_variable)}")
print(f"symmetric_difference of two set is {set_variable.symmetric_difference(New_set_variable)}")

set_variable.add(100)
print(set_variable)

set_variable.remove(100)
print(set_variable)