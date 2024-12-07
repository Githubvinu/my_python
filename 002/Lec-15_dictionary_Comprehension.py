from loguru import logger
logger.info("Lec-15_dictionary_Comprehension.py")

labour_with_cost = {
    "Mahesh": 500,
    "Ramesh": 400,
    "Mithilesh": 400,
    "Sumesh": 300,
    "Jagmohan": 1000,
    "Rampyare": 800
}

print(labour_with_cost)
logger.info(labour_with_cost["Jagmohan"])
#logger.info(labour_with_cost["Jagmohan1"])

logger.info(labour_with_cost.get("Jagmohan"))
logger.info(labour_with_cost.get("vinay"))

logger.info(labour_with_cost.keys())
logger.info(labour_with_cost.values())

logger.info(labour_with_cost.items())

#update
labour_with_cost.update({"vinay":920})
print(labour_with_cost)

#update with other way to merge two dictionary
new_dist = {"gannu":5000}
final_dist = {**labour_with_cost,**new_dist}
logger.info(final_dist)

#pop popitems
print(labour_with_cost)
print(labour_with_cost.pop("Mahesh"))
print(labour_with_cost)
print(labour_with_cost.popitem())
print(labour_with_cost)

#copy method
New_labour = labour_with_cost.copy()
print(New_labour)
print(id(labour_with_cost),id(New_labour))

#clear method
labour_with_cost.clear()
print(labour_with_cost)



# dictionary comprehension
dist_new = {
    "Mahesh": 500,
    "Ramesh": 400,
    "Mithilesh": 400,
    "Sumesh": 300,
    "Jagmohan": 1000,
    "Rampyare": 800
}
print(dist_new)
dist_new_1 = {i:dist_new[i]+100 for i in dist_new}
dist_new_2 = {i:dist_new.get(i)+200 for i in dist_new}
print(dist_new_1)
print(dist_new_2)

logger.info(dist_new)
dist_new_2 = {name: dist_new.get(name)+50 if name!="Jagmohan" else dist_new.get(name) for name in dist_new}
print(dist_new_2)


#how to get the character count
name = 'hello world'
char_cnt = {}
for chr in name:
    if chr in char_cnt:
        char_cnt[chr] += 1
    else:
        char_cnt[chr] = 1

print(char_cnt)