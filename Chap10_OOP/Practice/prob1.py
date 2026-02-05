#WAP to create a class called Programmer  for storing information of few programmers working at a microsft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language 

p = Programmer("Raaz", 120000, "Python")
print(p.name, p.salary, p.language)
q = Programmer("Rahul", 12000000, "Java")
print(q.name, q.salary, q.language)