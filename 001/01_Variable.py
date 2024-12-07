#variable
length = 100
weidth = 200

print(length,weidth)
# where these variable stored
print(id(length),id(weidth))

new_length = 100
print(new_length)
# for both same value has same address
print(id(length),id(new_length))

Length = 1000
Weidth = 2000
print(Length,length)
print(Weidth,weidth)


print("======================")

length_of_land = 100
bricks_cost_per_piece = 10.5
labour_name = "jagmohal"
is_home = True

print(length_of_land,bricks_cost_per_piece,labour_name,is_home)
print(type(length_of_land),type(bricks_cost_per_piece),type(labour_name),type(is_home))