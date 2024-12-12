result = None
a = float(input("Enter First Number: "))
b = float(input("Enter the Second Number "))

# Way 1
try:
    result = a / b
except:
    print("ZeroDivisionError: float division by zero")

print('result = ',result)
print("ENd of result")


# Way 2
result1 = None
try:
    result1 = a / b
except Exception as e:
    print("ERROR = ",e)
    print("ERROR = ",type(e))

print('result1 = ',result1)
print("ENd of result1")

# Way 3
result2 = None
try:
    result2 = a / b
except ZeroDivisionError as e:
    print("ERROR = ",type(e))

print('result2 = ',result2)
print("ENd of result2")


# Way 4
result3 = None
try:
    result3 = a / b
except ZeroDivisionError as e:
    print("ERROR = ",type(e))
except TypeError as e:
    print("TypeError = ",type(e))

print('result3 = ',result3)
print("ENd of result3")