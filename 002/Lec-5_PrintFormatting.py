print("string formatting and logging, escape sequence in python")

length_of_land = 100
cost_of_per_unit_price = 8.5
print('Length of land is',length_of_land)
print("Length of land is",length_of_land)
print("Length of \nland is:\n",length_of_land)
print('''Length 
      of 
      land
      is''',length_of_land)

print("My home is '3 BHK'",length_of_land)
print('My home is "4 BHK"',length_of_land)
print('My home \t is \'5 BHK\'',length_of_land)

# f String methon  and . method
print(f'Cost of per unit is {cost_of_per_unit_price}')
a = 11
b = 'hello'
c = 10.10
print('value of a is {}, b is {}, and c is {}'.format(a,b,c))

from loguru import logger
logger.info(f"this is value of B is {b}")
