# super keyword- call child class to parent class
# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")

# class ChildClass(ParentClass):
#     def parent_method(self):
#         print("Anushka")
#         super().parent_method()
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()

# child_object =ChildClass()
# child_object.child_method()
# child_object.parent_method()

class Employee:
    def __init__(self , name , id ,):
        self.name = name 
        self.id = id 

class Programmer(Employee):
    def __init_(self ,  name , id , lang):
        self.name = name
        super().__init__(name , id)   
        self.lang = lang     


aditya = Employee("Aditya" , 429)
anushka = Programmer("Anushka" , "8876" , "Python")
print(anushka.name)
print(anushka.id)
print(anushka.lang)



