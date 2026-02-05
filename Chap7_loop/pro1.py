# WAP to find the multiplication table of giver number

num = int(input("enter the number: "))
print("\nThe multiplication table of number", num, " are as follows: ")

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
    i +=1