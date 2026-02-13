#WAP to create a class Pets  from a class Animal  and further create a class Dog  from pets and 
# add  a method bark  to the class dog

class Animal:
    pass
class Pets(Animal):
    pass
class Dog(Pets):

    @staticmethod  #If you don't want to write self in the bark() method then you can use the staticmethod
    
    def bark():
        print("Bow Bow")
    pass

d = Dog()

d.bark()