# lecture 66 
# Instance and class variable 

class Employee:
    companyName  = "TATA" #class variable
    noofEmployee = 0
    def __init__(self , name ):
        
        self.name = name 
        self.raiseamount = 0.2 #instance variable
        Employee.noofEmployee +=1
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount {self.noofEmployee}  sized  in {self.companyName} is {self.raiseamount}")

emp1 = Employee("anu")
emp1.raiseamount = 0.8
emp1.companyName = "Apple"
emp1.showDetails() #second method - Employee.showDetails(emp1)
emp2 =Employee("Adi")
emp2.companyName = "Relance" 
emp2.showDetails()
# agr instance variable denge to vhi show krega otherwise class variable show krega


