from loguru import logger

labour_name = ["Mahesh","Suresh","Ramesh","Ganesh"]
logger.info(f"FULL List {labour_name}")

new_labour = ["DAMRU","GANNU","NAMAN"]

#adding two list with extend and +

# labour_name.extend(new_labour)
# print(labour_name)

labour_name = labour_name + new_labour
print(labour_name)

wage = [100,200,300,400,500,600,700]
labour_with_wage = labour_name + wage
print(labour_with_wage)

# access the range value
print(labour_with_wage[0:3])
print(labour_with_wage[6:8])
print(labour_with_wage[7:])
print(labour_with_wage[14:])
print(labour_with_wage[::-1])

#length
print(len(labour_with_wage))

#pop method delete the element from list
print(labour_with_wage.pop())
print(labour_with_wage)

print(labour_with_wage.pop(6))
print(labour_with_wage)

#remove method
print(labour_with_wage.remove('Ramesh'))
print(labour_with_wage)

print(labour_with_wage.remove(300))
print(labour_with_wage)


#delete the list
# del labour_with_wage
# print(labour_with_wage)

#update the list value
labour_with_wage[0]="MAHESH"
print(labour_with_wage)

labour_with_wage[0:5]=['MAHESH Ji', 'Suresh Ji', 'Ganesh Ji', 'DAMRU Ji', 'GANNU Ji']
print(labour_with_wage)

#Split Method
api_endpoint = "https://portal.azure.com/VMINSTANCE/test-vm/subs_id/aexy-234-mns/getCredential"

new_api_endpoint = api_endpoint.split("/")
print(new_api_endpoint)
print(new_api_endpoint[-1])
print(new_api_endpoint[-2])

