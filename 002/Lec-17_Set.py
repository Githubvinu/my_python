from loguru import logger
logger.info("*******SET********")

set1 = {1,2,7,8,4,12,2}
set2 = {2,4,6,5,15}
print(set1)
print(set2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
print(set1.isdisjoint(set2))
set2.add(100)
print(set2)
set2.remove(100)
print(set2)


#Q1. Given two lists, find the missing and additional values in both the lists.
#Input : 
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
#Output : 
# Missing values in list1 = [8, 7]
##Additional values in list1 = [1, 2, 3]
#Missing values in list2 = [1, 2, 3]
#Additional values in list2 = [7, 8]

missing_value_set1 = set(list2).difference(set(list1))
logger.info(f"Missing values in list1 = {missing_value_set1}")

Addational_value_set1 = set(list1).difference(set(list2))
logger.info(f"Additional values in list1 = {Addational_value_set1}")



#Q2. Given three arrays, we have to find common elements in three sorted lists using sets.
#Input : 
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3,4, 15,20,30,70,80, 120]
#Output : [80, 20]
print(list(set(ar3).intersection(set(ar1).intersection(set(ar2)))))

#without set, using loop
rslt_out=[]
for i in ar1:
    for j in ar2:
        for k in ar3:
            if i == j:
                if j ==k:
                    rslt_out.append(i)

logger.info(rslt_out)

new_out = []
for i in ar1:
    if i in ar2:
        if i in ar3:
            new_out.append(i)

logger.info(new_out)

