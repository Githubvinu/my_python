from loguru import logger

name = "viNAy SHarma"
lst = [10,20,30,40,50,60]

counter=0
for var in name:
    print(counter,var)
    counter+=1

print(name[:6])
print(name.capitalize())
print(name.count("a"))
print(name.count("N"))

print("A ASCII valye is:-",ord("A"))
print("Z ASCII valye is:-",ord("Z"))
print("a ASCII valye is:-",ord("a"))
print("z ASCII valye is:-",ord("z"))

print(chr(91)) #[
print(chr(92)) #\
print(chr(93))#]
print(chr(94))#^
print(chr(95))#_
print(chr(96))#_


print(name.endswith("a"))
print(name.endswith("s"))

name1= "vinay sharma"
name2= "Vinay Sharma"
name3= "VINAY SHARMA"
name4= "VInAy ShArMa"
print(name1.islower())
print(name2.islower())
print(name3.isupper())
print(name4.isupper())

new_name = name.replace("viNAy","SONU")
print(new_name)

print("VINAY SHARMA  ".strip())

print(name)
print(name.swapcase())

print("====================")
mail = input("Enter your mail id: ")
print(mail)
mail1,domain= mail.split("@")
encrypt_mail = mail1[0] + ("*"*(len(mail1)-2)) + mail1[len(mail1)-1]+"@"+domain
print(encrypt_mail)