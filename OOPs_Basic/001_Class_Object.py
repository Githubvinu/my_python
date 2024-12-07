class car:
    pass

ford = car()
honda = car()
tata = car()

ford.speed = 200
honda.speed = 300
tata.speed = 500

ford.color = 'red'
honda.color = 'blue'
tata.color = 'orage'

print("Ford data")
print(ford.speed)
print(ford.color)

print("TATA data")
print(tata.speed)
print(tata.color)

honda.color ='Yellow'
print(honda.color)