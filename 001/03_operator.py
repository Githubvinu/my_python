from loguru import logger
import math

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home = True

#calculate the total area of land

total_area_of_land = length_of_land * breadth_of_land
logger.info(f"Total area of my land id: {total_area_of_land} sq feet")

perimeter_of_land = 2 * (length_of_land + breadth_of_land)
logger.info(f"perimiter of land is: {perimeter_of_land} ft")

# print(15/6)
# print(15//6)
# print(math.floor(15/6))
# print(math.ceil(15/6))

a = 5
b = "10"
print(a + int(b))
print(str(a) +" "+b)

#user inputclear
user_area_length = float(input("Please enter yout home length:->"))
user_area_breadth =  input("Please enter yout home length:->")
total_area = user_area_length * float(user_area_breadth)
logger.info(f"total your home area id:-> {total_area}")