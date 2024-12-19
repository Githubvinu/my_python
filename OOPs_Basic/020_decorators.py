def decorator_fun(func):
    def wrapper_func():
        print('X' * 20)
        func()
        print('Y' * 20)

    return wrapper_func

@decorator_fun
def say_hello():
    print("Hello World")

# hello = decorator_fun(say_hello)
# hello()
say_hello()