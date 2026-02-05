# WAP to convert inches to centimeters using function 

def inch_to_centimeter():
    inches = float(input("Enter the value in inches: "))
    centimeters = inches * 2.54
    return centimeters

print(f"The value in centimeter is: {inch_to_centimeter()}")