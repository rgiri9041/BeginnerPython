class Employee:
        def __init__(self, language, salary): #Constructor with parameters
            #it is also known as dunder init method
            # Constructor is a special method which is called when an object of the class is created
            # It is used to initialize the attributes of the class
            # The __init__ method is called automatically when an object is created
            
            self.language = language
            self.salary = salary
        
        def getInfo(self):
            print(f"Language you are learning is {self.language} and salary is {self.salary}")

raaz = Employee("Python", 5000) # Creating an object of the class Employee with parameters
raaz.getInfo()