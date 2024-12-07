from loguru import logger
logger.info("******STRING***********")

name = 'VINAY SHARMA'
counter = 0
for i in name:
    print(counter,i)
    counter+=1
print(name[:4])

name1 = 'vinay sharma'
name2 = 'vInAy sHarma'
name3 = ' vinay shar ma '
print(name2.capitalize())
print(name1.count("a"))
print(name1.endswith("a"))
print(name1.endswith("y"))
print(name2.upper())
print(name2.lower())
print(name1.replace("vinay","sonu"))
print(len(name3))
print(name3.strip())
print(len(name3.strip()))
print(name2.swapcase())

name4 = "vinay sonu gannu bhalu vedu manan"
name5 = name4.split(" ")
print(name5)
endwithU=[]
for i in name5:
    if i.endswith("u"):
        endwithU.append(i)
    else:
        continue
print(endwithU)


#Q1. Swap the case of the string without using swapcase inbuilt method for string
Input = "Programming Aasan Hai"
#Output:- pROGRAMMING aASAN hAI 
output = ""
for i in Input:
    if i.islower():
        output=output+i.upper()
    else:
        output=output+i.lower()
print(Input)
print(output)

#Q3:
#Input :
#Mail,mob
#Renuka1992@gmail.com,9856765434 
#anbu.arasu3@gmail.com,9844567788 

#Output:
#Mail,mob
#R********2@gmail.com,98****34 
#a*********3@gmail.com,98****88
mobilenum = '9856765434'
print(mobilenum)
print(mobilenum[0]+(len(mobilenum)-2)*'*'+mobilenum[-1])

email = 'Renuka1992@gmail.com'
email_p1=email.split("@")[0]
email_p2=email.split("@")[1]
email_new=email_p1[0]+(len(email_p1)-2) * '*'+email_p1[-1]
print(email)
print(email_new+"@"+email_p2)


IPinput = [
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
"/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
"/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"
]

myout = []
for i in IPinput:
    a = i.split("/server/")[1].split("/")[0]
    myout.append(a)

print(list(set(myout)))
