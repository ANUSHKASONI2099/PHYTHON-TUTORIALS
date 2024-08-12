from k import info

# lecture 57

# Classes and objects 



# class Person:
#     name = "anushka"
#     occupation = "Software Developer"
#     networth = 10
#     def info(self):
        # print(f"{self.name} is {self.occupation}")

# a = Person()
# b = Person()
# a.name = "aditya"
# a.occupation = "Accountant"

# b.name = " aradhya"
# b.occupation =  "HR"

# a.info()
# b.info()

# print(a.name ,a.occupation)

# constructure is a unique function that gets called automatically
# lecture 58
class Person:
    def __init__(self , name , occ):
        print("Hey I am a person")
        self.name = name 
        self.occ = occ
    # name = "adi"
    # occ = "developer"

    def info(self):
        print(f"{self.name} is a {self.occ} " )

a = Person("Anushka" , "Devloper")
b = ("Aditya" , "HR")
a.info()
b.info()
