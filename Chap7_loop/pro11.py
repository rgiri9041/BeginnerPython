# WAP to print the multiplication table of a given number using both for

n = int(input("Enter the number: "))
print(f"The multiplication table of {n} is:  \n")
for i in range(1, 11):
    print(f"{n} X {i} = {n*i}")

# WAP to print using while loop 

m = int(input("Enter the number: "))
i = 10
print(f"The multiplication table of {m} is:  \n")
while i >= 1:
    print(f"{m} X {i} = {m*i}")
    i -= 1

    