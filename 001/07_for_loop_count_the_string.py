from loguru import logger

count = 0
paragraph = """Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry’s thought leader on the dimen
sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry’s best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the fi rst commercial product with windows, icons, 
and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University"""

paragraph_lst = paragraph.lower().split(" ")
print(paragraph_lst)

for letter in paragraph_lst:
    if letter == "the":
        count = count + 1
    else:
        continue

logger.info(f"total THE count is: {count}")

#==========insert 15 in list without any method========
# 1st Way
lst = [12, 76,89,165,202]
lst.append(15)
lst.sort()
print(lst)

#2nd Way
lst_1 = [12, 76,89,165,202]
index=0
logger.info(f"\n index value is {index}\n List Value is {lst_1}")

for i in range(len(lst_1)-1):
    if lst_1[i]>120:
        index=index
        logger.info(f"if loop value i is {i} and index value is {index}")
    else:
        index=index+1
        logger.info(f"Else loop value i is {i} and index value is {index}")

lst_1= lst_1 + [None]
print(lst_1)

for j in range(len(lst_1)-1,index,-1):
    print(f"J value is: {j}")
    print(f"list value is: {lst_1[j]}")
    lst_1[j]=lst_1[j-1]
print(lst_1)
lst_1[index]=120
print(lst_1)