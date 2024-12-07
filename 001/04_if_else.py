from loguru import logger

length_of_land = 100
breadth_of_land = 100
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home = True

length_of_land=int(input("Please enter your home area in sq feet:-> "))

if length_of_land<100:
    logger.info(f"We cant build your home in {length_of_land} feet area")
elif length_of_land>1000:
    logger.info(f"You can build {int(length_of_land/500)} bhk in this area")
else:
    logger.info("we will reach you for more information")