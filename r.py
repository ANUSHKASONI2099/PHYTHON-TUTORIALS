# topic - global variable and local variable


# x = 4
# print(x)


# def hello():
#     print(x)
#     print(f"the local x is {x}")
#     print("hello harry")


# print(f"the global x is{x}")
# hello()
# x = 5
# print(f"the global  is {x}")



x = 10 # global variable


def my_function():
    global x
    x = 4
    y = 5 #local variable 
    print(y)


my_function()
print(x)
print(y) # this will cause an error becouse  y is a local variable  and is not accesible outsideof the function


