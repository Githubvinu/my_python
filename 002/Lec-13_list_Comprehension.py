from loguru import logger
logger.info("This is for List Comprehension")

lst = list(range(1,20))
print(lst)

#get prime number in new list prmlst
prim_lst = []
for i in lst:
    if i % 2 ==0:
        prim_lst.append(i)

print(prim_lst)

#get prime number in new list prmlst in list comprehension
new_lst = [k for k in lst if k % 2 == 0]
logger.info(new_lst)

# Add prime and odd text for each value
statuslst = []
statuslst1 = []
for i in range(0,5):
    if i % 2 ==0:
        statuslst.append("EVEN")
        statuslst1.append((i,"EVEN"))
    else:
        statuslst.append("ODD")
        statuslst1.append((i,"ODD"))

logger.info(statuslst)
logger.info(statuslst1)

stat_lst = ["even" if i % 2 == 0 else "odd" for i in range(0,5)]
print(stat_lst)

stat_with_lst = [(i,'EvEn' if i%2==0 else 'Odd') for i in range(1,11)]
print(stat_with_lst)



