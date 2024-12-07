from loguru import logger
logger.info("Function")
a = 100
b = 50

def add(firstval,secondval):
    final = firstval + secondval
    return(final)

print(add(10,5))