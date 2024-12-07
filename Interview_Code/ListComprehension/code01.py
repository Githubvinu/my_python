#What will be the output of the following Python code?
l=[1,2,3,4,5]
print([x&1 for x in l])
#001 & 001 => 001 => 1
#001 & 010 => 000 => 0
#001 & 011 => 001 => 1
#001 & 100 => 000 => 0
#001 & 101 => 001 => 1
#===> [1,0,1,0,1]


l1=[1,2,3]
l2=[4,5,6]
print([x*y for x in l1 for y in l2])


s=["pune", "mumbai", "delhi"]
print([(w.upper(), len(w)) for w in s])


l1=[2,4,6]
l2=[-2,-4,-6]
for i in zip(l1, l2):
	print(i)
	
l1=[10, 20, 30]
l2=[-10, -20, -30]
l3=[x+y for x, y in zip(l1, l2)]
print(l3)


lst1=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print([x**3 for x in lst1])
print([x^3 for x in lst1])
print([x**3 in lst1])