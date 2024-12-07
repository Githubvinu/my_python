from loguru import logger
logger.info("dictionary")

labour_cost = {"ram":1000,"shyam":800,"mohan":300}
logger.info(labour_cost)
labour_cost["rampyare"]=550
labour_cost["harimohan"]=2000
logger.info(labour_cost)
logger.info(labour_cost.keys())
logger.info(labour_cost.values())
logger.info(labour_cost.items())

#how to access the dictionary way1
for name in  labour_cost:
    logger.info(f"{name},{labour_cost[name]}")

#how to access the dictionary way2
for key,value in labour_cost.items():
    logger.info(f"{key},{value}")