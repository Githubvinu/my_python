from loguru import logger

# simple for loop
new_list = []
for number in range(1,11):
    if number%2 == 0:
        new_list.append(number)


print(new_list)

#list comprehension way which help only if only condation

new_comp_list= [ number for number in range(1,11) if number%2==0]
print(new_comp_list)

print("=========================")
new_list_1 = []
for num1 in range(1,11):
    if num1%2==0:
        new_list_1.append("even")
    else:
        new_list_1.append("odd")

print(new_list_1)


#list comprehension with if else
new_list_2 = ["EVEN" if num2%2==0 else "ODD" for num2 in range(1,11)]
print(new_list_2)
