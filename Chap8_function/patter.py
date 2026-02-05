# WAP to print the pattern using function 

'''
***
**
*
    
'''
def pattern(num):
    if num == 0:
        return
    else:
        print("*" * num)

        pattern(num-1)
n = int(input("Enter the number: "))
print("The pattern is: " )
pattern(n)
