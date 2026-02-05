# WAP to find the multiplication table of a number entered by the user using while loop 

num = int(input("Enter the number: "))
i = 1
while i < 11:
    print(f"{num} X {i} = {num*i}")
    i += 1