result = None

a = float(input("Enter value of A: "))
b = float(input("Enter value of B: "))

try:
    result = a/b
except ZeroDivisionError as e:
    print("ZeroDivisionError = ",type(e))
except TypeError as e:
    print("TypeError = ",type(e))
else:
    print("=====ELSE=====")
finally:
    print("======FINALLY======")

print(f"result of {a} / {b} is : ",result)
print("===END==")