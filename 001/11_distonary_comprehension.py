from loguru import logger

labour_with_cost = {"Mahesh" : 500,
                    "Ramesh" : 400,
                    "Mithilesh" : 400,
                    "Sumesh" : 300,
                    "Jagmohan" : 1000,
                    "Rampyare" : 800}
print(labour_with_cost)

print(labour_with_cost["Mahesh"])
#print(labour_with_cost["Mahesh1"]) -- KeyError so we use get which throw none

print(labour_with_cost.get("Mahesh"))
print(labour_with_cost.get("Mahesh1"))

print(labour_with_cost.keys())
print(labour_with_cost.values())

print(labour_with_cost.items())
print(type(labour_with_cost.items()))

labour_with_cost.update({"Mahesh":510,"RAM":2000})
print(labour_with_cost)

new_dist = {"Mahesh":555,"RAM":2222}
final_dist = {**labour_with_cost,**new_dist}
print(final_dist)

#pop method
print(labour_with_cost)
print(labour_with_cost.pop("Mahesh"))
print(labour_with_cost.popitem())
print(labour_with_cost)

#copy method
labour_with_cost_copy = labour_with_cost.copy()
print(id(labour_with_cost))
print(id(labour_with_cost_copy))

#clear method
labour_with_cost.clear()
print(labour_with_cost)



print("==============dictionary comprehension ============")
#dictionary comprehension 

labourWithCost = {"Mahesh" : 500,
                    "Ramesh" : 400,
                    "Mithilesh" : 400,
                    "Sumesh" : 300,
                    "Jagmohan" : 1000,
                    "Rampyare" : 800}
print(labourWithCost)

labourWithNewCost = {key:value+100 for key,value in labourWithCost.items()}
print(labourWithNewCost)

labourWithNewCost_1 = {key:value if key=="Jagmohan" else value+100  for key,value in labourWithCost.items()}
print(labourWithNewCost_1)

#letter count and IN use
name ="vinayvinaysharmA"
letter_count = {}
for char in name:
    if char in letter_count:
        letter_count[char]+=1
    else:
        letter_count[char]=1
print(letter_count)


data = {"DERF":0,"POENKN":10,"DD":7,"MAINDATA":[{"IDD":"d3454355","BDD":"5678hfjhjh","LINKID":4,"HeaderFields":[{"FieldTypeName":"H1","Value":"false"},{"FieldTypeName":"H2","Value":"148877564"},{"FieldTypeName":"H3","Value":"20230930"},{"FieldTypeName":"H4","Value":"20231130"},{"FieldTypeName":"H5","Value":"2441.56"},{"FieldTypeName":"H6","Value":"0.00"},{"FieldTypeName":"H7","Value":"2411.56"},{"FieldTypeName":"H8","Value":"EUR"},{"FieldTypeName":"H9","Value":"00115190035"},{"FieldTypeName":"H10","Value":""},{"FieldTypeName":"H11","Value":"4500575382"},{"FieldTypeName":"H12","Value":"0.00"},{"FieldTypeName":"H13","Value":""},{"FieldTypeName":"H14","Value":""},{"FieldTypeName":"H15","Value":"F0"},{"FieldTypeName":"H16","Value":"87"},{"FieldTypeName":"H17","Value":"0.00"},{"FieldTypeName":"H18","Value":""},{"FieldTypeName":"H19","Value":""},{"FieldTypeName":"H20","Value":"No"}],"CodingLines":[],"Tables":[{"N1":"233553","N2":"3555","N3":"ASDDDD","N4":"334324","N5":"900.00","N6":"1.29","N7":"387.00","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""},{"N1":"765765","N2":"67657657","N3":"ADFDFF)","N4":"667657","N5":"1000.00","N6":"1.94","N7":"1940.00","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""},{"N1":"67657","N2":"76576576576","N3":"SFDFFDFSDF","N4":"7667676","N5":"1000.00","N6":"0.11456","N7":"114.56","N8":"","N9":"0.00","N10":"","N11":"","N12":"","N13":"","N14":""}],"INININ":"148877564","SDRER":"null"},{"IDD":"frret5","BDD":"5trtry4566","LINKID":4,"HeaderFields":[{"FieldTypeName":"H1","Value":"false"},{"FieldTypeName":"H2","Value":"ICI2300397"},{"FieldTypeName":"H3","Value":"20231219"},{"FieldTypeName":"H4","Value":"20240331"},{"FieldTypeName":"H5","Value":"76.44"},{"FieldTypeName":"H6","Value":"0.00"},{"FieldTypeName":"H7","Value":"76.44"},{"FieldTypeName":"H8","Value":"INR"},{"FieldTypeName":"H9","Value":"56676765"},{"FieldTypeName":"H10","Value":""},{"FieldTypeName":"H11","Value":"0.00"},{"FieldTypeName":"H12","Value":""},{"FieldTypeName":"H13","Value":""},{"FieldTypeName":"H14","Value":"F1"},{"FieldTypeName":"H15","Value":"87"},{"FieldTypeName":"H16","Value":"0.00"},{"FieldTypeName":"H17","Value":""},{"FieldTypeName":"H18","Value":""}],"CodingLines":[{"CODE1":0.0,"CODE2":76.44,"CODE3":"5645654","CODE4":"","CodingFields":[{"FieldName":"COL1","Value":"223DD666"},{"FieldName":"COL2","Value":"3454545"},{"FieldName":"COL3","Value":""},{"FieldName":"COL5","Value":""},{"FieldName":"COL5","Value":""}]}],"Tables":[],"INININ":"DER3434","SDRER":"null"}],"Final":"JKHJKLH0909908"}
print(data)


MAINDATA = {key:value for key,value in data.items() if key=="MAINDATA"}
logger.info(f"MAINDATA full data is {MAINDATA}")

#for value in MAINDATA