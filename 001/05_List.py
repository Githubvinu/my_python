from loguru import logger

labour_name = ["Mahesh","Suresh","Ramesh","Ganesh"]

logger.info(f"FULL List {labour_name}")
logger.info(f"First Element in the list is {labour_name[0]}")
logger.info(f"Last Element in the list is {labour_name[-1]}")

# appened Method the value
labour_name.append("RAM")
labour_name.append("SHAYMA")
logger.info(f"Full List data is : {labour_name}")

#insert Medhod
labour_name.insert(0,"SONU")
logger.info(f"Full List data is : {labour_name}")

#Extend Method
new_labour = ["DAMRU","GANNU","NAMAN"]
labour_name.extend(new_labour)
logger.info(f"Full List data is : {labour_name}")
logger.info(f"Last Element in the list is {labour_name[-1]}")

#multi dimensional list

labour_wih_wage = [["SONU",100],["MONU",500],["GANNU",200],["BHALU",300]]
logger.info(f"full multi dim list value is {labour_wih_wage}")
logger.info(f"{labour_wih_wage[1][0]} labour chage is : {labour_wih_wage[1][1]}")

