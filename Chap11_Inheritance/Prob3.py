#WAP to create a class Employee and  add salary and increment properties to it.
# '''Write a  method salaryAfterIncrement  method with a @property decorator with a setter which
# change the value based on increment'''

class Employee:
    salary = 2000
    incrementProperty = 20
    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.incrementProperty/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.incrementProperty = ((salary /self.salary) -1) *100

e = Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 2400.00
print(e.incrementProperty)

