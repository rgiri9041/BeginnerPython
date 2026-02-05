class Employee:
    language = "Python"
    salary = 5000

    def getInfo(self): # in a function one parameter is always required which is by default called self
        print(f"Language you are learning is {self.language} and salary is {self.salary}")

raaz = Employee()

raaz.getInfo()
