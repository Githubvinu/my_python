from loguru import logger
logger.info("Agrement and Key argement")

def sum(*value):
    rst=0
    for i in value:
        rst = rst + i   
    return(rst)

print(sum(1,2))
print(sum(1,2,3))
print(sum(1,2,3,4,10,20))

print("discount 10 percent on all production")

def discountfun(*arg,discount=0.1):
    total_actual_price=0
    for price in arg:
        total_actual_price=total_actual_price+price
    final_price_after_discount=total_actual_price - (total_actual_price*discount)
    return(final_price_after_discount)


print(discountfun(100,200,300))
print(discountfun(1000,2000,7000,12000))

