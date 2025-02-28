def myfunc1():
    x = "John"
    print(x)
    def myfunc2():
        nonlocal x
        x = "hello"
        print(x)  
        return x
x="Mirko"
print(x)
print(myfunc1())


