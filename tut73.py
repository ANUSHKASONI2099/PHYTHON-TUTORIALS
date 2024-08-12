# dunder/magic method - start with __ and end with __ 

# class Employee:
#     name = "aditya"
#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i+1
#         return i



# e = Employee()
# print(e.name)
# print(len(e))

class Employee:
    def __init(self , name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i
    def __str__(self):
        return f"The name of the employee is {self.name}"
    

    def __repr__(self):
        return f"Employee('{self.name}')"
    def __call__(self):
        print("i am fine")



