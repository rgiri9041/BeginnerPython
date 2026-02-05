# WAP to find the factorial of a given number 
num = int(input("Enter the number: "))
factorail = 1
if num < 0:
    print("Negative number do not have factoiral")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num+1):
        factorail *= i
        print(f"The factorial of {i} is {factorail}")