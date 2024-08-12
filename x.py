# lecture 59
# Decoraters
# def hello():
    # print("Hello everyone")

# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("good mrng!")
#         fx(*args, **kwargs)
#         print("Thanks for using this function")
#     return mfx

# @greet
# def hello():
#     print("hello")


# def add(a, b):
#     print(a+b)    

# hello()
# greet(hello)() 

# lecture 60 
# getters and setters 

class Myclass:
    def __init__(self,value):
        self._value = value

    def show(self):
            print(f"value is {self._value}")
    @property
    def ten_value(self):
            return 10* self._value
        

    @ten_value.setter
    def ten_value(self , new_value):
            self._value = new_value/10


obj = Myclass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()
    


