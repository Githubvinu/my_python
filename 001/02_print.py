length_of_land = 100
bricks_cost_per_piece = 10.5
labour_name = "jagmohal"
is_home = True

print("length of land is: ",length_of_land)
print('bricks cost per piece',bricks_cost_per_piece)

print("My flat is 2BHK. \nI am going to shift in next year")

print("""My flat is 2BHK.
I am going to shift in next year""")

print('''My flat is 2BHK.
I am going to shift in next year''')

# escale the special character
print("Hi, How are you sonu1")
print("Hi, How are you 'sonu2'")
print('Hi, How are you "sonu3"')
print("Hi, How are you \"sonu4\"")
print("Hi, How are you\t \"sonu4\"")

# String formatting
#f string , .formated method
print(f'My home information is :{length_of_land} {bricks_cost_per_piece} {labour_name}')
print("My home1 information is:{} {} {}".format(length_of_land,bricks_cost_per_piece,labour_name))

#loguru
#pip install loguru

from loguru import logger
logger.debug("That's it, beautiful and simple logging!")
logger.debug(f'My home information is :{length_of_land} {bricks_cost_per_piece} {labour_name}')
logger.info("That's it, beautiful and simple logging!")
logger.info(f'My home information is :{length_of_land} {bricks_cost_per_piece} {labour_name}')
