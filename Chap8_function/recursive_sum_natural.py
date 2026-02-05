# WAP to print the sum of first n natural number using function in recursion 

def sum(num):
    if num == 1:
        return 1
    else:
        return num +sum(num-1)
a = int(input("Enter the number: "))
print(f"The sum of first {a} natural number is  {sum(a)}")