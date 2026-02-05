class Employee:  # This is a class
	language = "Python"
	salary = 5000

raaz = Employee() # Creating an objec of the class Employee
raaz.language = "Java" 
# This is a object variable and it is not related to the class Employee alos it has higher priprity then class
print(raaz.language, raaz.salary)