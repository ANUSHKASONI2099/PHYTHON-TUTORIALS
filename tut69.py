
class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is  {self.company}")

@classmethod
def changeCompany(cls , newComapny):
    cls.company = newComapny


e1 = Employee()
e1.name  = "anushka"
e1.show()
# e1.changeCompany("tesla")
# e1.show()
# print(Employee.company)