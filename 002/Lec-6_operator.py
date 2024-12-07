from loguru import logger
logger.info("start the lec 6")

length_of_land = 100
breath_of_land = 100
todatl_home_land = length_of_land * breath_of_land
logger.info(f"Total of Land is : {todatl_home_land} sq ft")

a = 'hello'
b = '100'
print(a+b)

c = 11
d = 22
print(c+d)

e = '10'
f = 20
print(int(e)+f)
print(e+str(f))


length_of_new_land = float(input("please enter your new length: "))
breath_of_new_land = float(input("please enter your new breath_of_new_land: "))

logger.info(f'{type(length_of_new_land)}')
logger.info(f'{type(breath_of_new_land)}')
#total_land = length_of_new_land * breath_of_new_land
#total_land = int (length_of_new_land * breath_of_new_land)
total_land = abs (length_of_new_land * breath_of_new_land)
logger.info(f"Total land of area is {total_land} sq ft")