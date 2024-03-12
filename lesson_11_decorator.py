def my_decorator(func):
    def wrapper():
        print(type(func))
        print("Do something here")
        func()
        print("Original function is finished")
    return wrapper

@my_decorator
def myfunc():
    print("My name is Kalob")
    
@my_decorator
def myfunc2():
    print("My name is Michael") 

myfunc()
myfunc2()
