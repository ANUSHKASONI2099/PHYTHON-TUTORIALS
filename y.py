# lecture 61
# inheritence

# class Employee:
#     def __init__(self, name, id):
#         self.name = name 
#         self.id = id

#     def showDetails(self):
#         print(f"the name of employee: {self.id} is {self.name}")    

# class Devloper(Employee):
#     def showLanguage(self):
#         print("The default language is python")

# e1 = Employee("Anushka", 400)
# e1.showDetails()
# e2 = Devloper("Aditya",4100)
# e2.showDetails()



# Lecture 62  doubt
# access modifiers 
# publice access modifiers 
# private 
# protected 

# class Employee :
#     def __init__(self):
#         self.__name = "anu"

# a = Employee()
# # print(a.__name) cannot be accesed directly
# print(a._Employee__name) # can be accessed indirectly 
# print(a.__dir__())


# lecture 63 
# solution of ex.5

# lecture 64
# ex 5 

# lecture 65 
# static method 

class Math :

    def __init__(self , num):
        self.num = num
    def addtonum(self , n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a+b
    
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)


print(a.add(7,5)) # alg hai ye method
