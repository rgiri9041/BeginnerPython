#WAP to metho 'salaryAfterIncrement' method with  a @property decorator with a setter which change the value of increment based on salary

class Employee():
    salary = 1000
    increment = 100

    @property  #it directly allow or provide the salary value
    def salaryAfterIncrement(self):
        return(self.salary + self.salary *(self.increment /100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100
    

    
a = Employee()
#print(a.salaryAfterIncrement)

a.salaryAfterIncrement = 2000
print(a.increment)