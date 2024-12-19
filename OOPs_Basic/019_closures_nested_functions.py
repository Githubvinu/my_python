def outerFunction(text):
    def InnerFunction():
        print(text)
    return InnerFunction

a = outerFunction("Hello")

a()



def nth_power(exponent):
    def pow_of(base):
        return pow (base, exponent)
    return pow_of

square = nth_power(2)
print(square(2))
print(square(3))
print(square(4))
print(square(5))
