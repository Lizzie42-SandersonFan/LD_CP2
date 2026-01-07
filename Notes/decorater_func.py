# LD 1st Example of decorator function

def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

@decorator
def greet():
    print("Hello World")

greet()

@decorator
def add():
    print(1+1)

add()