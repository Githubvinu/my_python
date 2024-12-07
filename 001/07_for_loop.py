from loguru import logger

labour_name = ["Mahesh","Suresh","Ramesh","Ganesh"]
logger.info(f"full list value is: {labour_name}")

for name in labour_name:
    logger.info(f"{name}")

print("==================================")

for i in range(len(labour_name)):
    logger.info(f"Labour {i+1} name is: {labour_name[i]}")

print("**********************************")
for j in range(10):
    print((j+1) * "* ")

print("odd & even number")
for number in range(101):
    if (number%2==0):
        logger.info(f"{number} is EVEN")
    else:
        logger.info(f"{number} is ODD")


print("************abc*****************")
for k in range(5):
    print((5-k) * "* ")