# object introspection 
# dir() dict() help method use to find what presrnt in obects 

# dir() methods - return all a list of all the attributes and methods including "dunder methos" - __ vale 

x = (1,2,3)
print(dir(x))
print(x.__add__)

# dict() mthods attributes jo use hue a hai as a dictionary ajayenge.
class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        
p = Person("john" , 30)
print(p.__dict__)

# Help metod - 
class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        
p = Person("john" , 30)
print(help(Person))