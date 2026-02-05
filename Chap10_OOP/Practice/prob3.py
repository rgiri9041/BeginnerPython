#WAP to use the static method in a class

class demo:

    @staticmethod # static method does not take self as parameter
    def greet():
        print("Hello there, welcome to static method")

demo.greet() # Calling static method using class name
a = demo()
a.greet()