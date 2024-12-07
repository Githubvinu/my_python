from loguru import logger

labout_with_cost = {"Mahesh":500,"Ramesh":400,"mithlesh":600,"parmesh":800}
logger.info(f"{labout_with_cost}")

labout_with_cost["Jagmohan"]=1000
labout_with_cost["Balram"]=1200
logger.info(f"{labout_with_cost}")

labout_with_cost["Mahesh"]=550
logger.info(f"{labout_with_cost}")

logger.info(labout_with_cost.keys())
logger.info(labout_with_cost.values())

#itergate the distonery values
print(labout_with_cost)
for name in labout_with_cost:
    logger.info(f"{name},{labout_with_cost[name]}")

for key,value in labout_with_cost.items():
    logger.info(f"{key},{value}")

print("=========Start==============")
logger.info(f"Full labour distonary is {labout_with_cost}")
total_cost=0
for i in range(1,51):
    for key,value in labout_with_cost.items():
        total_cost=total_cost+value
        logger.info(f"day {i} total cost is {total_cost}")

logger.info(f"Total_cost is : {total_cost}")

mahesh_absent = labout_with_cost["Mahesh"] * 3
logger.info(f"mahesh absent cost is : {mahesh_absent}")

Jagmohan_absent = labout_with_cost["Jagmohan"] * 7
logger.info(f"Jagmohan absent cost is : {Jagmohan_absent}")

final_total_cost = total_cost-(mahesh_absent+Jagmohan_absent)
logger.info(f"final total cost  is : {final_total_cost}")
print("=========End==============")

