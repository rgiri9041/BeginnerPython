# WAP to find the factorial of given number using both for and while loop
n = int(input("Enter the number: "))
fact = 1
print("Using for loop:")
for i in range(1, n+1):
    fact *= i
    print(f"the factoiral of {i} is {fact}")
    i += 1

#while loopp
print("\nUsing while loop:")
num = int(input("Enter the number: "))
facto = 1
i =1
while i <= num:
    facto *= i
    print(f"The factorial of {i} is {facto}")
    