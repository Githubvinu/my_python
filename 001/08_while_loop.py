from loguru import logger
import time


labour_name = ["Mahesh","Suresh","Ramesh","Ganesh"]
print(labour_name)

print("=========================================================")
name_itr = 0
while(name_itr<len(labour_name)):
    print(labour_name[name_itr])
    name_itr+=1

print("=========================================================")

name_itr1 = len(labour_name)-1
while(name_itr1>=0):
    logger.info(f"iteration value is:{name_itr1}")
    print(labour_name[name_itr1])
    name_itr1=name_itr1-1

print("=========================================================")
name_itr2 = 0
while(name_itr2<len(labour_name)):
    print(labour_name[name_itr2])
    time.sleep(10)
    name_itr2+=1




