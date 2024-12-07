from loguru import logger
logger.info("This is for look second part")

paragraph = """ Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry’s thought leader on the dimen
sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry’s best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the fi rst commercial product with windows, icons, 
and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University """
print(paragraph)

para = paragraph.split(" ")
print(para)

thelst = []
notthelist = []
for name in para:
    if name.lower() == "the":
        thelst.append(1)
    else:
        notthelist.append(1)

logger.info(f"paragraph total count value is {len(para)}")
logger.info(f"the count value is {len(thelst)}")
logger.info(f"without the count value is {len(notthelist)}")


print("**********************************************")
lst = [202, 165, 89, 76, 12]
number_to_insert = 15

cnt1 = 0
cnt2 = 0
for i in lst:
    if (i > number_to_insert):
        cnt1 = cnt1 + 1
    else:
        cnt2 = cnt2 + 1

print(cnt1)
print(cnt2)
print(lst[:cnt1])
print(lst[cnt1:len(lst)])

newlst1 = lst[:cnt1]
newlst = [number_to_insert]
newlst2 = lst[cnt1:len(lst)]
print(newlst1)
print(newlst)
print(newlst2)

final_lst = newlst1 + newlst + newlst2
print(final_lst)

