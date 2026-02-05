# WAP to Convert celsius to fahrenheit using function

def ctf():
    celsius = float(input("Enter the temperaure in elsius: "))
    farh = (celsius * 9/5) + 32
    return farh

print(f"The temperature in fahrenheit is: {ctf()}")