#Create a classs pets from class Animals and further create a class dogs from cclass pets . add a method bark to the class dog

class Animals():
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    #@staticmethod ---> if you don't want to use the self then you can use static method 
    def bark(self):
        print("The dog is doinng Bow Bow!")

a = Dog()
a.bark()